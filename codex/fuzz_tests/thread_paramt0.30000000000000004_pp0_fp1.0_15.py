import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 2\n')).start()

# Example 2
import sys, threading
def f():
    sys.stdout.write('Hello from thread 1\n')
threading.Thread(target=f).start()

# Example 3
import sys, threading
def f():
    sys.stdout.write('Hello from thread 1\n')
thread = threading.Thread(target=f)
thread.start()

# Example 4
import sys, threading
def f():
    sys.stdout.write('Hello from thread 1\n')
thread = threading.Thread(target=f)
thread.start()
thread.join()

# Example 5
import sys, threading
def f():
    sys.stdout.write('Hello from thread 1\n')
thread = threading.Thread(target=f)
thread.start()
thread.join()
print('thread ended')

# Example 6
import sys
