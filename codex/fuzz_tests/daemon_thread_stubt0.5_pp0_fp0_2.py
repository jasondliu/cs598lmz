import sys, threading

def run():
    sys.stdout.write("%s\n" % threading.currentThread().getName())

t1 = threading.Thread(target=run)
t2 = threading.Thread(target=run)

t1.start()
t2.start()

t1.join()
t2.join()
