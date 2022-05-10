import select
# Test select.select
'''
select.select(readlist, writelist, xlist, [timeout])
'''
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 2222))
s.listen(10)
s.setblocking(0)

epoll = select.epoll()

epoll.register(s.fileno(), select.EPOLLIN)

connections = {}
addresses = {}
try:
    while True:
        events = epoll.poll(1)
        for fileno, event in events:
            if fileno == s.fileno():
                conn, addr = s.accept()
                print("Connected", addr)
                conn.setblocking(0)
                epoll.register(conn.fileno(), select.EPOLLIN)
                connections[conn.fileno()] = conn
                addresses[conn.fileno()] = addr
            elif event & select.EPOLLIN:
                data = connections[fileno].rec
