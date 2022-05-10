import select
# Test select.select()

def slow_systemcall():
    select.select([], [], [], 0.1)

start = time.time()
for _ in range(5):
    slow_systemcall()
end = time.time()
print('Took %.3f seconds' % (end - start))

# Test ThreadPoolExecutor

from concurrent import futures

def slow_systemcall():
    select.select([], [], [], 0.1)

start = time.time()
with futures.ThreadPoolExecutor(max_workers=5) as e:
    e.map(slow_systemcall, range(5))
end = time.time()
print('Took %.3f seconds' % (end - start))

# Test ProcessPoolExecutor

from concurrent import futures

def slow_systemcall():
    select.select([], [], [], 0.1)

start = time.time()
with futures.ProcessPoolExecutor(max_workers=5) as e:
    e.map(slow_systemcall, range(5))
end = time
