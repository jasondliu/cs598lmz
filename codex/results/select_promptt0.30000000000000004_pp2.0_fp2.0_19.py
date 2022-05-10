import select
# Test select.select()

def slow_systemcall():
    select.select([],[],[],0.1)

start = time.time()
for _ in range(5):
    slow_systemcall()
end = time.time()
print('Took %.3f seconds' % (end-start))

# Test threading

def compute_helicopter_location(index):
    pass

for i in range(5):
    compute_helicopter_location(i)

# Test multiprocessing

import multiprocessing

start = time.time()

processes = []
for _ in range(5):
    p = multiprocessing.Process(target=compute_helicopter_location,
                                args=(i,))
    p.start()
    processes.append(p)

for p in processes:
    p.join()

end = time.time()
print('Took %.3f seconds' % (end-start))

# Test multiprocessing with a pool

start = time.time()

pool = multip
