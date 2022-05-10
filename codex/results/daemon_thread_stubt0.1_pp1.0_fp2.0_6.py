import sys, threading

def run():
    while True:
        print("Hello")

thread = threading.Thread(target=run)
thread.start()

while True:
    print("World")
</code>
I would expect the output to be:
<code>World
Hello
World
Hello
World
Hello
...
</code>
However, the output is:
<code>World
World
World
...
</code>
Why is the thread not running?


A:

You need to call <code>thread.join()</code> in order to wait for the thread to finish.
<code>import sys, threading

def run():
    while True:
        print("Hello")

thread = threading.Thread(target=run)
thread.start()

while True:
    print("World")

thread.join()
</code>

