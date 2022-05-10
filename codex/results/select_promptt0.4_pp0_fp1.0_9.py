import select
# Test select.select()

import time

start = time.time()

timeout = 5
readable, writable, exceptional = select.select(
    [sys.stdin], [], [], timeout)

if not (readable or writable or exceptional):
    print("Time out ! ")
else:
    print("ready !")

end = time.time()
print(end - start)

# 测试 select.poll()

import select
import os
import time

start = time.time()

poll = select.poll()
poll.register(sys.stdin, select.POLLIN)

while True:
    events = poll.poll(10000)
    if events:
        print("ready !")
        break
    else:
        print("Time out ! ")

end = time.time()
print(end - start)

# 测试 select.epoll()

import select
import os
import time

start = time.time()

epoll = select.epoll()
epoll.register(sys.stdin
