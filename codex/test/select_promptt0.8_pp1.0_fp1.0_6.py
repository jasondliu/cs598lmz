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
