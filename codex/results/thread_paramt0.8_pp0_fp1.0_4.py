import sys, threading
threading.Thread(target=lambda: sys.stdout.write('thread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('thread 2\n')).start()
threading.Thread(target=lambda: sys.stdout.write('thread 3\n')).start()

# thread.start_new_thread
import sys
thread.start_new_thread(lambda: sys.stdout.write('thread 1\n'), ())
thread.start_new_thread(lambda: sys.stdout.write('thread 2\n'), ())
thread.start_new_thread(lambda: sys.stdout.write('thread 3\n'), ())

# multiprocessing
import multiprocessing
multiprocessing.Process(target=lambda: sys.stdout.write('process 1\n')).start()
multiprocessing.Process(target=lambda: sys.stdout.write('process 2\n')).start()
multiprocessing.Process(target=lambda: sys.stdout.write('process 3\n')).start()
