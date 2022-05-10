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
But instead I get:
<code>World
World
World
World
World
World
...
</code>
I'm running this on Windows 10, Python 3.7.3.
What am I doing wrong?


A:

You need to flush the output buffer.
<code>import sys, threading

def run():
    while True:
        print("Hello")
        sys.stdout.flush()

thread = threading.Thread(target=run)
thread.start()

while True:
    print("World")
    sys.stdout.flush()
</code>

