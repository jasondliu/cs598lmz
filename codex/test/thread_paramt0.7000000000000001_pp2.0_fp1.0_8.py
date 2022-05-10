import sys, threading
threading.Thread(target=lambda: sys.stdout.write("Hello from a thread\n")).start()

# Multiprocessing

import multiprocessing, math

def isprime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

primes = []
def primesum(n):
    primes.append(sum(i for i in range(n) if isprime(i)))

t = time.time()
nprocs = 8
with multiprocessing.Pool(processes=nprocs) as pool:
    pool.map(primesum, [10000000] * nprocs)
print(time.time() - t)

# Asynchronous programming

# Threads

import threading

def wait_for_event(name):
    print(f'Event {name} is starting')
    time.sleep(1)
    print(f'Event {name} is finished')
