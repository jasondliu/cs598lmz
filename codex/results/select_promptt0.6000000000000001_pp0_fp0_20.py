import select
# Test select.select
print('Trying select.select')
for i in range(5):
    read, write, err = select.select([sock], [sock], [sock])
    print('Read:', read)
    print('Write:', write)
    print('Error:', err)

# Test select.poll
print('\nTrying select.poll')
p = select.poll()
p.register(sock, select.POLLIN | select.POLLOUT)
for i in range(5):
    print('  poll:', p.poll(1000))

# Test select.epoll
print('\nTrying select.epoll')
e = select.epoll()
e.register(sock.fileno(), select.EPOLLIN | select.EPOLLOUT)
for i in range(5):
    print('  epoll:', e.poll(1))
