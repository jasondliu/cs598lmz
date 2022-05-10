import socket
# Test socket.if_indextoname
# Tokenize

import socket
def read_file(filename):
    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content


def tokenize(content):
    tokens = []
    for i in range(len(content)):
        tokens.append(re.findall(r'[\w\\\\]+', content[i]))
    return tokens
# LocalTest.py /home/kaseywang/socketTest/testcases/case1.txt 1
# LocalTest.py /home/kaseywang/socketTest/testcases/case2.txt 1 
import sys
import socket
def socketTest(i, debug, client_server, content, ip, port, family, type1):
    success = True
    i = int(i)
    debug = int(debug)
    client_server = int(client_server)
    ip = str(ip)
    port = int(port)
    family = int(family)
    type1 = int(type1)

