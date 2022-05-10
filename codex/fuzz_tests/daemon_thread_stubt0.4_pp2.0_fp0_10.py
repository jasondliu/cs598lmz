import sys, threading

def run():
    try:
        while True:
            sys.stdout.write('%s\n' % threading.currentThread().getName())
            sys.stdout.flush()
    except KeyboardInterrupt:
        pass

for i in range(5):
    t = threading.Thread(target=run)
    t.start()
