import sys, threading

def run():
    print('hello')

if __name__ == '__main__':
    while True:
        threading.Timer(3, run).start()
</code>
I want to print the string <code>'hello'</code> every 3 seconds. It doesn't work. 
How can I make it work?


A:

<code>Python</code> <code>threading.Timer</code> is a subclass of <code>threading.Thread</code>, so you can do something like this:
<code>from threading import Timer
import time

def hello():
    print "hello, world"
    t = Timer(3.0, hello)
    t.start() # after 30 seconds, "hello, world" will be printed

t = Timer(3.0, hello)
t.start()
</code>

