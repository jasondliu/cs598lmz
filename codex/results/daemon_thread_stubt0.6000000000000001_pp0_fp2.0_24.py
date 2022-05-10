import sys, threading

def run():
    print "hello"
    sys.exit()

threading.Thread(target=run).start()

print "goodbye"
</code>
This prints out "hello" and then "goodbye" immediately, rather than after the thread has exited. I've also tried <code>threading.Thread(target=run).join()</code>, but that results in a deadlock.
How do I get the main thread to wait for the thread to exit?


A:

The thread exits before the main program gets a chance to print goodbye.
<code>import sys, threading

def run():
    print "hello"
    sys.exit()

threading.Thread(target=run).start()

threading.Thread(target=print, args=["goodbye"]).start()
</code>

