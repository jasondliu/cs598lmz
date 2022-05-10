import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(map(str, range(1000000))))).start()

# The above code will print all the numbers from 1 to 1 million, but it will take a long time.
# This is because the print() function is thread safe, which means it can only be used by one thread at a time.
# The thread that calls print() will acquire a lock, print the numbers, and release the lock.
# Meanwhile, the main thread will wait for the lock to be released.
# The main thread will then acquire the lock, print the numbers, and release the lock.
# The process repeats until all the numbers have been printed.
# This is a waste of time because the main thread could have been doing the printing itself.
#
# To avoid this problem, we can replace the print() function with sys.stdout.write().
# sys.stdout.write() is not thread safe.
# This means that multiple threads can use it at the same time.
# The main thread will acquire the lock, print the numbers, and release the lock.
# Meanwhile, the other thread will acquire the lock, print the numbers,
