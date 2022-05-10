import sys, threading

def run():
    print("Thread started")
    while True:
        pass

thread = threading.Thread(target=run)
thread.start()

print("Thread running")
sys.exit()
</code>
The output is:
<code>Thread running
Thread started
</code>
I want to wait for the thread to start before exiting.
I tried <code>thread.join()</code> but it doesn't work.
How can I do it?


A:

You can use <code>thread.is_alive()</code> to check if the thread is running.
<code>import sys, threading

def run():
    print("Thread started")
    while True:
        pass

thread = threading.Thread(target=run)
thread.start()

while thread.is_alive():
    pass

print("Thread running")
sys.exit()
</code>

