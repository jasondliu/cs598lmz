import sys, threading

def run():
    while True:
        print("Hello World")
        time.sleep(1)

def main():
    thread = threading.Thread(target=run)
    thread.start()
    print("Hello")
    time.sleep(5)
    sys.exit()

if __name__ == "__main__":
    main()
</code>
The output is:
<code>Hello
Hello World
Hello World
Hello World
Hello World
Hello World
</code>
I would like to know how to make the program exit after the 5 seconds and not print the other "Hello World"s.


A:

You can use <code>thread.join()</code> to wait for the thread to finish.
<code>import time
import sys
import threading

def run():
    while True:
        print("Hello World")
        time.sleep(1)

def main():
    thread = threading.Thread(target=run)
    thread.start()
    print("Hello")
    time.sleep(5)
    thread.join()

if __name__ ==
