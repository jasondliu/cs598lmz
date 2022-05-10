import select
# Test select.select()
# 1. create pipes and sockets

# 5. create a random pipe and socket
r, w = os.pipe()
r_obj = select.epoll()
r_obj.register(r, select.EPOLLIN)

# 3. create a random pair of tcp sockets
s_obj1, s_obj2 = socket.socketpair()
s_obj1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s_obj2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s_obj1.setblocking(False)
s_obj2.setblocking(False)

s_obj1.bind(('127.0.0.1', 8090))
s_obj2.bind(('127.0.0.1', 8091))

