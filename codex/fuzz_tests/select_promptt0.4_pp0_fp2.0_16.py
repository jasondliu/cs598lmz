import select
# Test select.select()

def slow_systemcall():
    select.select([], [], [], 0.1)

start = time.time()
for i in range(5):
    slow_systemcall()
end = time.time()
print(end - start)

# Using threads

from threading import Thread

def compute():
    return sum([i**2 for i in range(20000000)])

start = time.time()
compute()
end = time.time()
print(end - start)

threads = []
for i in range(5):
    threads.append(Thread(target=compute))
    threads[-1].start()

for thread in threads:
    thread.join()

end = time.time()
print(end - start)

# Using processes
from multiprocessing import Process

procs = []
for i in range(5):
    procs.append(Process(target=compute))
    procs[-1].start()

for proc in procs:
    proc.join()

end = time
