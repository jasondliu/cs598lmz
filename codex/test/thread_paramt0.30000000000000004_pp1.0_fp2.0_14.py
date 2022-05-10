import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(map(str, range(100000))))).start()

# from multiprocessing import Process
# Process(target=lambda: sys.stdout.write('\n'.join(map(str, range(100000))))).start()

# import threading
# threading.Thread(target=lambda: sys.stdout.write('\n'.join(map(str, range(100000))))).start()

# import multiprocessing
# multiprocessing.Process(target=lambda: sys.stdout.write('\n'.join(map(str, range(100000))))).start()

# import multiprocessing
# multiprocessing.Process(target=lambda: sys.stdout.write('\n'.join(map(str, range(100000))))).start()

# import multiprocessing
# multiprocessing.Process(target=lambda: sys.stdout.write('\n'.join(map(str, range(100000))))).start()

# import multiprocessing
# multiprocess
