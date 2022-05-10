import select
# Test select.select()

def slow_systemcall():
    select.select([], [], [], 0.1)

start = time.time()
for i in range(5):
    slow_systemcall()
end = time.time()
print('Took %.3f seconds' % (end - start))

# Test ThreadPoolExecutor

from concurrent import futures

def slow_systemcall():
    select.select([], [], [], 0.1)

start = time.time()
with futures.ThreadPoolExecutor(max_workers=5) as executor:
    f1 = executor.submit(slow_systemcall)
    f2 = executor.submit(slow_systemcall)
    f3 = executor.submit(slow_systemcall)
    f4 = executor.submit(slow_systemcall)
    f5 = executor.submit(slow_systemcall)
end = time.time()
print('Took %.3f seconds' % (end - start))

# Test ProcessPoolExecutor

from concurrent import futures

