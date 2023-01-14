import socket
import threading
bind_ip= "0.0.0.0"
bind_port = 9998
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip,bind_port))
server.listen(5)
print(f'[*] Listening on {bind_ip}:{bind_port}')
def handle_client(client_socket):
    with client_socket as sock:
        # print out what the client sends
        request = client_socket.recv(1024)
        print(f'[*] Received: {request.decode("utf-8")}')        # send back a packet
        client_socket.send("ACK!".encode(encoding='utf-8'))
        client_socket.close()

while True:
    client,addr = server.accept()
    print(f'[*] Accepted connection from {addr[0]}:{addr[1]}')# spin up our client thread to handle incoming data
    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()
def handle_client(client_socket):
    with client_socket as sock:
        # print out what the client sends
        request = client_socket.recv(1024)
        print ("[*] Received: %s" % request)
        # send back a packet
        client_socket.send("ACK!".encode(encoding='utf-8'))
        client_socket.close()
