import select
# Test select.select
import socket, time

def slow_systemcall():
    select.select([socket.socket()], [], [], 0.1)

start = time.time()
for x in range(5):
    slow_systemcall()
end = time.time()
print('Took %.3f seconds' % (end - start))

# Test select.poll
start = time.time()
for x in range(5):
    select.poll().poll(0.1)
end = time.time()
print('Took %.3f seconds' % (end - start))

# Test select.epoll
start = time.time()
epoll = select.epoll()
for x in range(5):
    epoll.poll(0.1)
end = time.time()
print('Took %.3f seconds' % (end - start))

# Test select.kqueue
start = time.time()
kqueue = select.kqueue()
for x in range(5):
    kqueue.control([], 0.1)
end = time.time()
