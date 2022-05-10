import sys, threading

def run():
    while True:
        sys.stdout.write('%s\n' % threading.currentThread().getName())
        sys.stdout.flush()

t = threading.Thread(target=run)
t.start()

t = threading.Thread(target=run)
t.start()

t = threading.Thread(target=run)
t.start()
