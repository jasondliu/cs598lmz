import sys, threading

def run():
    while True:
        sys.stdout.write('0')
        sys.stdout.flush()
        time.sleep(1)

def run2():
    while True:
        sys.stdout.write('1')
        sys.stdout.flush()
        time.sleep(1)

t1 = threading.Thread(target=run)
t1.start()

t2 = threading.Thread(target=run2)
t2.start()
