import select
# Test select.select

import socket
from select import select

#server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 5000))
server.listen(5)
inputs=[server]

while True:
    print('while')
    rs, ws, es=select.select(inputs, [], [], 0.05)
    for r in rs:
        if r is server:
            client, addr=r.accept()
            inputs.append(client)
            print('new connection')
        else:
            data=r.recv(1024)
            if data:
                print('recv', data)
            else:
                inputs.remove(r)
                r.close()
                print('close')
