import sys, threading

def run():
    print "Running..."
    sys.stdout.flush()
    time.sleep(3)
    print "Done"
    sys.stdout.flush()

def main():
    t = threading.Thread(target=run)
    t.start()
    print "Thread started"
    sys.stdout.flush()
    t.join()

main()
</code>
This code starts a thread and prints "Thread started", but it never prints "Done".
If I change the <code>time.sleep(3)</code> to <code>time.sleep(1)</code> it prints "Done".
Why is this?


A:

The problem is not with the threading, but with the way you are using <code>stdout</code>.
In my python 2.7.3, the code runs fine with 3 second delay.
But, in python 2.7.5, the code does not print anything after the <code>Thread started</code> message.
The reason is that in python 2.7.5, <code>sys.stdout</code> is a <code>buff
