import sys, threading
threading.Thread(target=lambda: sys.stdout.write("hi\n")).start()
print(threading.activeCount())
print(threading.enumerate())
print(threading.currentThread())

threading.Thread(target=lambda: sys.stdout.write("bye\n")).start()
print(threading.activeCount())
print(threading.enumerate())
print(threading.currentThread())
