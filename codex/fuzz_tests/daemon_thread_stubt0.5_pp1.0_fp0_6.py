import sys, threading

def run():
    print("Hello from new thread")

thread = threading.Thread(target=run)
thread.start()
print("Hello from main thread")
</code>
The output is:
<code>Hello from main thread
Hello from new thread
</code>
As you can see, the main thread prints the message first and then the new thread. However, if I add <code>thread.join()</code> to the end of the code, the output is:
<code>Hello from new thread
Hello from main thread
</code>
Why does the main thread wait for the new thread to finish even though it is not asked to?


A:

The main thread will wait for all of its child threads to complete before exiting.

