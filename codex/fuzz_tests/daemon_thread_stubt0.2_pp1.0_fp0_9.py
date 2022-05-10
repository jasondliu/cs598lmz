import sys, threading

def run():
    while True:
        print("Hello")
        time.sleep(1)

if __name__ == "__main__":
    thread = threading.Thread(target=run)
    thread.start()
    while True:
        print("World")
        time.sleep(1)
</code>
I would expect the output to be:
<code>World
Hello
World
Hello
...
</code>
But instead I get:
<code>World
World
World
World
...
</code>
What am I doing wrong?


A:

You need to call <code>thread.join()</code> to wait for the thread to finish.
<code>import time
import sys, threading

def run():
    while True:
        print("Hello")
        time.sleep(1)

if __name__ == "__main__":
    thread = threading.Thread(target=run)
    thread.start()
    while True:
        print("World")
        time.sleep(1)
    thread.join()
</code>

