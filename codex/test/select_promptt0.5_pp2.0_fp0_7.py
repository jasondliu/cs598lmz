import select
# Test select.select
import time

start = time.time()
while True:
    (rl, wl, el) = select.select([sys.stdin], [], [], 1)
    if rl:
        print("You said", sys.stdin.readline().rstrip())
    # print("Looping")
    end = time.time()
    if end - start > 10:
        break

# Test select.poll
import select
import time
import sys

poll = select.poll()
poll.register(sys.stdin, select.POLLIN)

start = time.time()
while True:
    events = poll.poll(1000)
    if events:
        print("You said", sys.stdin.readline().rstrip())
    # print("Looping")
    end = time.time()
    if end - start > 10:
        break
