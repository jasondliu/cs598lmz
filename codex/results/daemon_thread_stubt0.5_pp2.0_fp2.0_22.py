import sys, threading

def run():
    while True:
        print "Running..."
        time.sleep(1)

def main():
    thread = threading.Thread(target=run)
    thread.start()

    while True:
        print "Main thread running..."
        time.sleep(1)

if __name__ == "__main__":
    main()
</code>
When I run this program, I see the following output:
<code>Main thread running...
Running...
Running...
Running...
Running...
Running...
Running...
Running...
Running...
</code>
And then it just hangs.  What am I not understanding about how threads work?


A:

You need to call <code>thread.join()</code> in order to wait for the thread to finish.

