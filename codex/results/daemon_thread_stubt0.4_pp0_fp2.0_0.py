import sys, threading

def run():
    print(threading.current_thread().name)
    sys.exit()

t = threading.Thread(target=run)
t.start()
t.join()
print(threading.current_thread().name)
</code>
I am expecting the output to be:
<code>Thread-1
MainThread
</code>
However, the actual output is:
<code>Thread-1
</code>
What is going on here?


A:

This is because <code>sys.exit()</code> is killing the entire process, not just the thread.

