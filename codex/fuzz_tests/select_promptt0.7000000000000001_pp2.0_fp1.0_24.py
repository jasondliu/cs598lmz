import select
# Test select.select()
s = socket.socket()
s.bind(('', 0))
s.listen(1)
s.setblocking(0)

pollster = select.poll()
pollster.register(s, select.POLLIN)

fd = s.fileno()
sock_map = {fd: s}

while True:
    events = pollster.poll(1000)
    for fd, flag in events:
        s = sock_map[fd]
        if flag & (select.POLLIN | select.POLLPRI):
            if s is server:
                # A "readable" server socket is ready to accept a connection
                connection, client_address = s.accept()
                connection.setblocking(0)
                fd = connection.fileno()
                sock_map[fd] = connection
                pollster.register(fd, select.POLLIN)
            else:
                data = s.recv(1024)
                if data:
                    # A readable client socket has data
                    print data
                else:
                    # Interpret empty result as closed connection
