import select
# Test select.select function

import socket
import select

s = socket.socket()
s.bind(('0.0.0.0', 2222))
s.listen(10)

socks = [s]

while True:
    r, w, e = select.select(socks, socks, socks)
    print('r:', r, 'w:', w, 'e:', e)
    if s in r:
        conn, addr = s.accept()
        socks.append(conn)
        print('accepted', addr)
    elif s in e:
        print('exception')
    else:
        print('other event')
    for sock in r:
        if sock is s:
            continue
        data = sock.recv(1024)
        if not data:
            print('closing connection')
            socks.remove(sock)
            sock.close()
        else:
            print(data.decode('utf-8'))
            sock.send(b'OK\n')

import socket
import select

s = socket.socket
