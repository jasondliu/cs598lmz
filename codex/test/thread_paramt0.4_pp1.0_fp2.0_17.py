import sys, threading
threading.Thread(target=lambda: sys.stdout.write("Hello from thread 1\n")).start()
threading.Thread(target=lambda: sys.stdout.write("Hello from thread 2\n")).start()

# 
#     $ python threading_hello.py
#     Hello from thread 2
#     Hello from thread 1
# 
# Here, we start two threads that each print a message. The output is interleaved
# because the two threads are executing concurrently.
# 
# If you want to wait for a thread to finish in the main program, use the
# `join()` method.
# 
#     >>> t = threading.Thread(target=lambda: sys.stdout.write("Hello from thread\n"))
#     >>> t.start()
#     >>> t.join()
#     Hello from thread
# 
# If you are creating a large number of threads, use a `ThreadPoolExecutor` to
# limit the number of threads in the pool.
# 
#     >>> from concurrent.futures import ThreadPoolExecutor
#     >>> pool = ThreadPoolExecutor(max_
