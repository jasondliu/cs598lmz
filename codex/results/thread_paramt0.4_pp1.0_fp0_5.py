import sys, threading
threading.Thread(target=lambda: sys.stdout.write(input())).start()

# from threading import Thread
# t = Thread(target=lambda: sys.stdout.write(input()))
# t.start()
# t.join()

# from multiprocessing import Process
# p = Process(target=lambda: sys.stdout.write(input()))
# p.start()
# p.join()
