import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Thread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Thread 2\n')).start()

#  $ python2 thread_target.py
# Thread 1
# Thread 2


# Threads will run simultaneously when the GIL is released
import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Thread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Thread 2\n')).start()
time.sleep(1)

# $ python2 thread_target_sleep.py
# Thread 1
# Thread 2


# When the GIL is released, threads are scheduled by the operating system.
# This can result in unexpected thread scheduling behavior.
# For example, in the following code:
import sys, threading, time
threading.Thread(target=lambda: sys.stdout.write('Thread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Thread 2\n')).start()
