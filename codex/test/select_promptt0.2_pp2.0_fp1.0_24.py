import select
# Test select.select()

def slow_systemcall():
    select.select([], [], [], 0.1)

start = time.time()
for i in range(5):
    slow_systemcall()
end = time.time()
print('Took %.3f seconds' % (end - start))

# Test select.poll()

start = time.time()
for i in range(5):
    select.poll()
end = time.time()
print('Took %.3f seconds' % (end - start))

# Test select.epoll()

start = time.time()
for i in range(5):
    select.epoll()
end = time.time()
print('Took %.3f seconds' % (end - start))

# Test select.kqueue()

start = time.time()
for i in range(5):
    select.kqueue()
end = time.time()
print('Took %.3f seconds' % (end - start))

# Test select.devpoll()

