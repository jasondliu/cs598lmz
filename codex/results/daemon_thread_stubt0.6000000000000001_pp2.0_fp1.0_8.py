import sys, threading

def run():
    sys.stdout.write('Thread started\n')
    sys.stdout.flush()
    sys.stdin.read(1)
    sys.stdout.write('Thread ended\n')
    sys.stdout.flush()

if __name__ == '__main__':
    thread = threading.Thread(target=run)
    thread.start()
    sys.stdout.write('Main thread\n')
    sys.stdout.flush()
    thread.join()
</code>
It will not print "Thread ended", but it will print "Main thread".

