import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from Thread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from Thread 2\n')).start()

# The output from these two threads may be interleaved in any fashion,
# because they are running in parallel, not in series.
# This is a classic example of Python’s “batteries included” nature,
# and its emphasis on programmer productivity and efficiency.
