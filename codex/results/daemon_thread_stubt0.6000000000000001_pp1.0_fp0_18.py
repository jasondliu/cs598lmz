import sys, threading

def run():
    sys.stdout.write('Hello from thread %s\n' % threading.currentThread())

t = threading.Thread(target=run)
t.start()
