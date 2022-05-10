import select
# Test select.select
import time
start = time.time()
while True:
    print(time.time() - start)
    r, w, e = select.select([sys.stdin], [], [], 5)
    if r:
        s = sys.stdin.readline()
        print('you entered {}'.format(s))
    else:
        print('timeout')
        break

# Test select.poll
import select
import time

poll = select.poll()
poll.register(sys.stdin, select.POLLIN)

while True:
    events = poll.poll(5)
    if events:
        s = sys.stdin.readline()
        print('you entered {}'.format(s))
    else:
        print('timeout')
        break

# Test select.epoll
import select
import time

epoll = select.epoll()
epoll.register(sys.stdin.fileno(), select.EPOLLIN)

while True:
    events = epoll.poll(5)
