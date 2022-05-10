import select
# Test select.select()

def slow_systemcall():
    select.select([], [], [], 0.1)

start = time.time()
for _ in range(5):
    slow_systemcall()
end = time.time()
print('Took %.3f seconds' % (end - start))

# Took 0.505 seconds

from functools import partial

def slow_systemcall():
    select.select([], [], [], 0.1)

start = time.time()
for _ in range(5):
    slow_systemcall()
end = time.time()
print('Took %.3f seconds' % (end - start))

# Took 0.505 seconds

from multiprocessing import Pool

pool = Pool()
start = time.time()
for _ in range(5):
    pool.apply_async(slow_systemcall)
end = time.time()
print('Took %.3f seconds' % (end - start))

# Took 0.101 seconds

from multiprocessing import Pool


