import sys, threading

def run():
    sys.stdout.write('This is stdout text\n')

def run2():
    sys.stderr.write('This is stderr text\n')

t1 = threading.Thread(target=run)
t2 = threading.Thread(target=run2)
t1.start()
t2.start()
t1.join()
t2.join()
