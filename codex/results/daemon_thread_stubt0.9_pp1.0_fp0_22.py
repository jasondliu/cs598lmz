import sys, threading

def run():
    sys.stdout.write("start\n")
    sys.stdout.flush()
    time.sleep(2)
    sys.stdout.write("stop\n")
    sys.stdout.flush()


if __name__ == '__main__':
    thread = threading.Thread()
    thread.daemon = True
    thread.run = run
    thread.start()
    time.sleep(1)
    sys.stdout.write("main\n")
    sys.stdout.flush()
    time.sleep(4)
</code>
Then I saw all 3 prints output: start, main, stop
So far so good, my question is, how exactly does the daemon attribute work?
From my test you can see:

daemon attribute must be set before starting the thread
daemon attribute only affects the output of the main thread, not the subprocess (here is the <code>time.sleep(2)</code>)

I appreciate your help!


A:

The main thread is not affected by the daemon at all. The main thread is a non-daemon thread by
