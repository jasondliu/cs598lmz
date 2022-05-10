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
p = select.poll()
for i in range(5):
    p.poll()
end = time.time()
print('Took %.3f seconds' % (end - start))

# Test select.epoll()

start = time.time()
e = select.epoll()
for i in range(5):
    e.poll()
end = time.time()
print('Took %.3f seconds' % (end - start))

# Test select.kqueue()

start = time.time()
k = select.kqueue()
for i in range(5):
    k.control([], 0)
end = time.time()
print('Took %.3f seconds'
