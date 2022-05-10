import select
# Test select.select()
import socket
s = socket.socket()
s.bind(('127.0.0.1',6789))
s.listen(5)
s.setblocking(0)

while True:
    rs,ws,es = select.select([s],[],[],1)
    print rs
    if rs:
        conn,addr = s.accept()
        print conn,addr
