import select
# Test select.select
import select
import time

start = time.time()

while True:
    ready = select.select([sys.stdin], [], [], 1)
    if ready[0]:
        print(sys.stdin.readline())
    else:
        print('%5.2f: %s' % (time.time() - start, 'spam'))

# Test select.poll
import select
import time

start = time.time()

poll = select.poll()
poll.register(sys.stdin, select.POLLIN)

while True:
    ready = poll.poll(1000)
    if ready[0][1] & select.POLLIN:
        print(sys.stdin.readline())
    else:
        print('%5.2f: %s' % (time.time() - start, 'spam'))

# Test select.epoll
import select
import time

start = time.time()
