import select
# Test select.select() by polling stdin.
while True:
    readable, writable, exceptional = select.select([sys.stdin], [], [], 1)
    if readable:
        s = sys.stdin.readline()
        print('Read:', s)
    else:
        print('Timed out')
 

# Test select.poll() by polling stdin.
import select
poll_object = select.poll()
poll_object.register(sys.stdin, select.POLLIN)
while True:
    if poll_object.poll(1000):
        s = sys.stdin.readline()
        print('Read:', s)
    else:
        print('Timed out')


# Test select.epoll() by polling stdin.
import select
epoll_object = select.epoll()
epoll_object.register(sys.stdin, select.EPOLLIN)
