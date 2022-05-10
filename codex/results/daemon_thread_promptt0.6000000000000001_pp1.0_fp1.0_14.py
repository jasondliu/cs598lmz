import threading
# Test threading daemon

def is_prime(num):
    for i in xrange(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def primes_in_range(start, end):
    for num in xrange(start, end):
        if is_prime(num):
            print num

def main():
    # This is the main thread
    thread_pool = []
    for i in xrange(2, 10):
        thread = threading.Thread(target=primes_in_range, args=[i*1000, (i+1)*1000])
        thread.start()
        thread_pool.append(thread)
    for thread in thread_pool:
        thread.join()

main()
