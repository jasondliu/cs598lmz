import sys, threading
threading.Thread(target=lambda: sys.stdout.write(threading.current_thread.getName())).start()

# def test(n):
#     i = 0
#     while i < n:
#         i += 1

# n = 10000
# threading.Thread(target=test, args=(n,)).start()
# test(n)

# from threading import Event, Timer
# from random import randint
# e = Event()
# def cb():
#     if randint(0, 1):
#         print 'EGG'
#         e.set()
#     else:
#         print 'SPAM'
#         e.clear()

# Timer(2, cb, ()).start()
# e.wait()

# from threading import Event, Timer
# from random import randint
# e = Event()
# def cb():
#     if randint(0, 1):
#         print 'EGG'
#         e.set()
#     else:
#         print 'SPAM'
#         e.clear()

# Tim
