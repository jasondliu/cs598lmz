import sys, threading

def run():
    print("hello")

thread = threading.Thread(target=run)
thread.start()

print("world")
</code>
This prints "hello", then "world".
What I need is a way to print "world", then have it wait until the thread has finished and print "hello".
Is there any way to do this?

