import threading
# Test threading daemon

def test():
    print("test")

def main():
    t = threading.Timer(3.0, test)
    t.daemon = True
    t.start()
    print("main")

main()
</code>
When I run this code, I expected the program to print "main" and then exit.  I expected the thread to be a daemon thread, so when the main thread exits, the thread would be terminated.  However, the program prints "main" and then "test" and then exits.
Why is the thread not terminated when the main thread exits?  Is there a way to make it terminate?


A:

<code>t.daemon = True</code> doesn't work like you think it does.
When you set <code>t.daemon</code> to <code>True</code>, you're telling Python that it's OK to kill <code>t</code> at any time, even if it's in the middle of doing something. In your case, the thread is just sitting there doing nothing, waiting for the timer to expire. So, when the main thread exits, Python doesn't
