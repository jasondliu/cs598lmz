import sys, threading

def run():
    while True:
        print('Hello from thread %s' % threading.get_ident())
        sys.stdout.flush()

thread = threading.Thread(target=run)
thread.daemon = True
thread.start()

while True:
    print('Hello from thread %s' % threading.get_ident())
    sys.stdout.flush()
</code>

