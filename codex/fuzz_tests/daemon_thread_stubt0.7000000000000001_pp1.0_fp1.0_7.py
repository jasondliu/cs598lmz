import sys, threading

def run():
    for i in range(10):
        sys.stderr.write("%d\n" % i)
    sys.stderr.flush()

threading.Thread(target=run).start()

while True:
     pass
