import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Thread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Thread 2\n')).start()

# Python 3.2+
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    executor.submit(lambda: sys.stdout.write('Thread 1\n'))
    executor.submit(lambda: sys.stdout.write('Thread 2\n'))

# Python 3.2+
with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executor:
    executor.submit(lambda: sys.stdout.write('Thread 1\n'))
    executor.submit(lambda: sys.stdout.write('Thread 2\n'))

# Python 3.2+
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    future1 = executor.submit(lambda: sys.stdout.write('Thread 1\n'))
