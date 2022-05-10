import sys, threading

def run():
    for i in range(5):
        print(i)
        time.sleep(1)

t = threading.Thread(target=run)
t.start()
</code>
However, I would like to run it asynchronously (i.e. not block the main thread) and without using a separate file. I tried the following, but it doesn't work:
<code>import time, sys, threading

def run():
    for i in range(5):
        print(i)
        time.sleep(1)

t = threading.Thread(target=run())
t.start()
</code>
How do I do this?


A:

In your example you call the function. You have to pass the function itself to <code>target</code> and not the result of the function call.
<code>t = threading.Thread(target=run)
</code>

