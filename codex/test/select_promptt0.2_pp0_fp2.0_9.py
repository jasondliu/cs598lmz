import select
# Test select.select()

def slow_systemcall():
    select.select([], [], [], 0.1)

start = time.time()
for _ in range(5):
    slow_systemcall()
end = time.time()
print('Took %.3f seconds' % (end - start))

# Test time.sleep()

start = time.time()
for _ in range(5):
    time.sleep(0.1)
end = time.time()
print('Took %.3f seconds' % (end - start))

# Test gevent.sleep()

import gevent

start = time.time()
for _ in range(5):
    gevent.sleep(0.1)
end = time.time()
print('Took %.3f seconds' % (end - start))

# Test gevent.select()

start = time.time()
for _ in range(5):
    gevent.select.select([], [], [], 0.1)
end = time.time()
