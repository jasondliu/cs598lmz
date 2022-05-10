import sys, threading
threading.Thread(target=lambda: sys.stdout.write("Hello from thread 1\n")).start()
threading.Thread(target=lambda: sys.stdout.write("Hello from thread 2\n")).start()
threading.Thread(target=lambda: sys.stdout.write("Hello from thread 3\n")).start()

# Python 2.x:
# import threading
# threading.Thread(target=lambda: sys.stdout.write("Hello from thread 1\n")).start()
# threading.Thread(target=lambda: sys.stdout.write("Hello from thread 2\n")).start()
# threading.Thread(target=lambda: sys.stdout.write("Hello from thread 3\n")).start()

# Python 3.x:
# import _thread as thread
# thread.start_new_thread(lambda: sys.stdout.write("Hello from thread 1\n"), ())
# thread.start_new_thread(lambda: sys.stdout.write("Hello from thread 2\n"), ())
# thread.start_new_thread(lambda: sys.stdout.write
