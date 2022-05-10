import sys, threading

def run():
    sys.stdout.write("%s: %s\n" % (threading.currentThread().getName(), threading.currentThread().isDaemon()))
    threading.currentThread().setDaemon(True)
    sys.stdout.write("%s: %s\n" % (threading.currentThread().getName(), threading.currentThread().isDaemon()))

t = threading.Thread(target=run)
t.start()

sys.stdout.write("%s: %s\n" % (threading.currentThread().getName(), threading.currentThread().isDaemon()))
threading.currentThread().setDaemon(True)
sys.stdout.write("%s: %s\n" % (threading.currentThread().getName(), threading.currentThread().isDaemon()))
