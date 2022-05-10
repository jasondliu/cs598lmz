import sys, threading

def run():
    try:
        while True:
            sys.stdout.write('%s\n' % threading.current_thread().name)
            sys.stdout.flush()
            time.sleep(1)
    except KeyboardInterrupt:
        sys.exit()

if __name__ == '__main__':
    t = threading.Thread(target=run)
    t.start()

    try:
        while True:
            sys.stdout.write('%s\n' % threading.current_thread().name)
            sys.stdout.flush()
            time.sleep(1)
    except KeyboardInterrupt:
        sys.exit()
</code>
This code produces:
<code>MainThread
Thread-1
Thread-1
MainThread
Thread-1
Thread-1
MainThread
Thread-1
Thread-1
MainThread
Thread-1
Thread-1
MainThread
Thread-1
Thread-1
MainThread
Thread-1
Thread-1
MainThread
Traceback (most recent call last):
  File "threads.py
