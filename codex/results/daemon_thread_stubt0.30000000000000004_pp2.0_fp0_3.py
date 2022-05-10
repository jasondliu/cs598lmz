import sys, threading

def run():
    print("run")
    sys.exit()

t = threading.Thread(target=run)
t.start()
t.join()

print("end")
</code>
When I run this code, it prints <code>run</code> and then <code>end</code>. I was expecting it to print <code>run</code> and then exit the program. Why doesn't it exit the program?


A:

<code>sys.exit()</code> exits the current thread.
<code>threading.Thread.join</code> waits for the thread to exit.
So you're exiting the thread, then waiting for the thread to exit.

