import sys, threading

def run():
    while 1:
        print 2

t = threading.Thread(target = run)
t.daemon = True
t.start()

while 1:
    print 1
    sys.stdout.flush()
    time.sleep(1)
