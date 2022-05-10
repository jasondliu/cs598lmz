import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(map(str, range(100000))))).start()

# This is the thread that will execute concurrently.
def countdown(n):
    while n > 0:
        n -= 1

# Create and launch a thread
t = threading.Thread(target=countdown, args=(10**7,))
t.start()

# Wait for the thread to complete
t.join()

# Check whether the thread is still alive
print(t.is_alive())

# Create and launch a thread
t = threading.Thread(target=countdown, args=(10**7,))
t.start()

# Check whether the thread is still alive
print(t.is_alive())

# Wait for the thread to complete
t.join()

# Check whether the thread is still alive
print(t.is_alive())

# Create and launch a thread
t = threading.Thread(target=countdown, args=(10**7,))
t.start()

# Get the identifier of the thread
tid = t
