import sys, threading

def run():
    while True:
        sys.stdout.write('\r%s' % threading.currentThread().getName())
        sys.stdout.flush()
        time.sleep(1)

def main():
    threads = []
    for i in range(5):
        threads.append(threading.Thread(target=run))
        threads[-1].start()
    for thread in threads:
        thread.join()

if __name__ == '__main__':
    main()
</code>
The output will be like:
<code>Thread-4Thread-1
Thread-2
Thread-3
Thread-0
</code>
But I want:
<code>Thread-1
Thread-2
Thread-3
Thread-4
Thread-0
</code>
How can I fix this?


A:

Use <code>threading.Lock</code> to avoid the threads from simultaneously writing to standard output:
<code>import time
import sys, threading

lock = threading.Lock()

def run():
    while True:
        with
