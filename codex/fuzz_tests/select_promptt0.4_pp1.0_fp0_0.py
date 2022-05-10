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

start = time.time()
threads = []
for i in range(5):
    threads.append(threading.Thread(target=compute_helicopter_location, args=(i,)))
    threads[-1].start()

for i in range(5):
    threads[i].join()
end = time.time()
print('Took %.3f seconds' % (end-start))

# Test multiprocessing
start = time.time()
processes = []
for i in range(5):
    processes.append(mp.Process(target=compute_helicopter_location, args=(i,)))
    processes[-1].start()

for
