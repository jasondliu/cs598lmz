import sys, threading
threading.Thread(target=lambda: sys.stdout.write(input())).start()

# from threading import Thread
# t = Thread(target=lambda: input())
# t.daemon = True
# t.start()
# print('hello')
# t.join()

# from multiprocessing import Process
# p = Process(target=lambda: input())
# p.start()
# print('hello')
# p.join()

# import sys
# sys.stdout.write(input())

# import sys, threading
# threading.Thread(target=lambda: sys.stdout.write(input())).start()
