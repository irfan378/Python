from scapy.all import TCP,rdpcap
import collections
import os
import re
import sys
import zlib

OUTDIR='/root/Desktop/pictures'
PCAPS='root/Downloads'

Response=collections.namedtuple('Response',['header','payload'])
def get_header(payload):
    try:
        header_raw=payload[:payload.index(b'\r\n\r\n')+2]
    except ValueError:
        sys.stdout.write('-')
        sys.stdout.flush()
        return None
    header=dict(re.findall(r'(?P<name>.*?): (?P<value>.*?)\r\n', header_raw.decode()))
    if 'Content-Type' not in header:
        return None
    return header
def extract_content(Response,content_name='image'):
    content,content_type=None,None
    if content_name in Response.header['Content-Type']:
        content_type = Response.header['Content-Type'].split('/')[1]
        content = Response.payload[Response.payload.index(b'\r\n\r\n')+4:]
        if 'Content-Encoding' in Response.header:
            if Response.header['Content-Encoding'] == "gzip":
                content = zlib.decompress(Response.payload, zlib.MAX_WBITS | 32)
            elif Response.header['Content-Encoding'] == "deflate":
                content = zlib.decompress(Response.payload)
    return content_type,content
class Recapper:
    def __init__(self,fname):
        # read the pcap file 
        pcap=rdpcap(fname)
        #seperate each TCP session in dict.
        self.sessions=pcap.sessions()
        # create an empty list called responses that we’re about to fill in with the responses from the pcap file
        self.responses=list()

    def get_response(self):
        #iterate over the sessions dictionary
        for session in self.sessions:
            payload=b''
            #iterate over the packets within each session
            for packet in self.sessions[session]:
                try:
                    #filter the traffic so we only get packets with a destination or source port of 80
                    if packet[TCP].dport==80 or packet[TCP].sport==80:
                        #concatenate the payload of all of the traffic into a single buffer called payload. This is effectively the same as right-clicking a packet in Wireshark and selecting Follow TCP Stream.
                        payload += bytes(packet[TCP].payload)
                except IndexError:
                    sys.stdout.write('x')
                    sys.stdout.flush()
            if payload:
                #we pass it off to the HTTP header-parsing function get_header, which enables us to inspect the HTTP headers individually.
                header=get_header(payload)
                if header is None:
                    continue
                #append the Response to the responses list
                self.responses.append(Response(header=header, payload=payload))

    def write(self,content_name):
        for i,response in enumerate(self.responses):
            content, content_type = extract_content(response, content_name)
            if content and content_type:
                fname = os.path.join(OUTDIR, f'ex_{i}.{content_type}')
                print(f'Writing {fname}')
                with open(fname, 'wb') as f:
                    f.write(content)
if __name__ == "__main__":
    pfile=os.path.join(PCAPS,"pcap.pcap")
    recapper=Recapper(pfile)
    recapper.get_responses()
    recapper.write('image')