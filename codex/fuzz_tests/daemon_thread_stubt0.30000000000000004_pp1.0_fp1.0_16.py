import sys, threading

def run():
    while True:
        print("Hello")
        time.sleep(1)

def main():
    thread = threading.Thread(target=run)
    thread.start()

if __name__ == '__main__':
    main()
</code>
I have tried using <code>thread.join()</code> but it just freezes the program. I have also tried using <code>thread.daemon = True</code> but it just kills the thread.
I am using Python 3.5.2.


A:

You can use <code>thread.daemon = True</code> but you need to make sure that the main thread doesn't exit before the daemon thread is done.
<code>import time
import sys, threading

def run():
    while True:
        print("Hello")
        time.sleep(1)

def main():
    thread = threading.Thread(target=run)
    thread.daemon = True
    thread.start()
    thread.join()

if __name__ == '__main__':
    main()
</code>

