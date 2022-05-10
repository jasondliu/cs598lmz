import threading
threading.current_thread()

def thread_function(name):
    print("Thread {}: starting".format(name))
    time.sleep(2)
    print("Thread {}: finishing".format(name))

if __name__ == "__main__":
    print("Main    : before creating thread")
    x = threading.Thread(target=thread_function, args=(1,))
    print("Main    : before running thread")
    x.start()
    print("Main    : wait for the thread to finish")
    # x.join()
    print("Main    : all done")

########################################################################################################################

import concurrent.futures
import math

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]

def is_prime(n):
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(
