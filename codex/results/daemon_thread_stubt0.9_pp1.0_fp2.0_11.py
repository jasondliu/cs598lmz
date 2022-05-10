import sys, threading

def run():
    while True:
        input()
        sys.stdout.write('stdout from thread1\n')

t1 = threading.Thread(target=run)
t2 = threading.Thread(target=run)
t1.start()
t2.start()
