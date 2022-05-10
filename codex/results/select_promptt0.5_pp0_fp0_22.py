import select
# Test select.select()

from socket import *
s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 20000))
s.listen(5)

while True:
    client, addr = s.accept()
    print "Got connection from", addr
    while True:
        data = client.recv(1024)
        if not data: break
        client.send(data)
    client.close()
