import threading
threading.stack_size(2**27)


class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        super(MyThread, self).run()


def num_prime(m):
    nprimes = 0
    k = m*(10**6)
    n = 2
    while n < k:
        if prime(n) == 'prime':
            nprimes += 1
        n += 1

    return nprimes

def prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return False
    k = int(pow(n, 0.5))
    for j in range(3, k + 1, 2):
        if n % j == 0:
            return False
    return 'prime'

def calc_primes(s):
    threads = [MyThread() for _ in range(s)]
    for i in range(s):
        threads[i].start()
    nprimes
