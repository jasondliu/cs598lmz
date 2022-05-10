import sys, threading

def run():
    while True:
        print "running"
        time.sleep(1)

t = threading.Thread(target=run)
t.start()
t.join()
</code>
When I run this, it prints <code>running</code> every second until I press Ctrl+C, which raises a <code>KeyboardInterrupt</code>. 
I'd like to catch the <code>KeyboardInterrupt</code> in the thread and gracefully exit the program. 
I tried this:
<code>def run():
    while True:
        try:
            print "running"
            time.sleep(1)
        except KeyboardInterrupt:
            sys.exit(1)
</code>
But this doesn't work. If I press Ctrl+C, it prints <code>running</code> once more and then exits. 
How can I catch the <code>KeyboardInterrupt</code> in the thread and exit gracefully?


A:

You can't. A thread can only catch exceptions that are raised in that thread. 
However, you can pass an event object to the thread
