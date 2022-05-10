import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 2\n')).start()

# Python 2.x
import sys, thread
thread.start_new_thread(lambda: sys.stdout.write('Hello from thread 1\n'), ())
thread.start_new_thread(lambda: sys.stdout.write('Hello from thread 2\n'), ())

# Python 3.x
import sys, _thread
_thread.start_new_thread(lambda: sys.stdout.write('Hello from thread 1\n'), ())
_thread.start_new_thread(lambda: sys.stdout.write('Hello from thread 2\n'), ())

# Python 2.x
import sys, thread
thread.start_new_thread(lambda: sys.stdout.write('Hello from thread 1\n'), ())
thread.start_new_thread(lambda: sys.stdout.write('Hello from thread 2\n'), ())

# Python 3.x
import sys, _thread
_thread
