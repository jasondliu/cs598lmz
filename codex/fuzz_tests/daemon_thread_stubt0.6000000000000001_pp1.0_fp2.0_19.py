import sys, threading

def run():
    print("Thread started")
    sys.stdout.flush()
    time.sleep(0.1)

if __name__ == '__main__':
    print("Starting thread")
    sys.stdout.flush()
    thread = threading.Thread(target=run)
    thread.start()
    thread.join()
    print("Thread finished")
    sys.stdout.flush()
</code>
You should see the following output:
<code>Starting thread
Thread started
Thread finished
</code>
In my case, it is also printed with colors, but that's not important.
Now, let's modify the code to use the <code>multiprocessing</code> module:
<code>import multiprocessing
import sys, time

def run():
    print("Thread started")
    sys.stdout.flush()
    time.sleep(0.1)

if __name__ == '__main__':
    print("Starting thread")
    sys.stdout.flush()
    process = multiprocessing.Process(target=run)
    process
