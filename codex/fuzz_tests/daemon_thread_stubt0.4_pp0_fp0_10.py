import sys, threading

def run():
    while True:
        print("Hello")

thread = threading.Thread(target=run)
thread.start()

while True:
    print("World")
</code>
I want to print <code>Hello</code> and <code>World</code> in an infinite loop. But when I run the program, it only prints <code>World</code> in an infinite loop.
How can I fix this?


A:

You need to add <code>thread.join()</code> to the end of your program. This will allow the main thread to wait for the other thread to complete before exiting.
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

