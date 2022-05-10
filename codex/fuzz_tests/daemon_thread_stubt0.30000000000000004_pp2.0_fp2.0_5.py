import sys, threading

def run():
    print("Hello from new thread")
    return

t = threading.Thread(target=run)
t.start()

print("Hello from main thread")
</code>
I am running this code on a Windows 10 machine with Python 3.7.1.
When I run this code, the output is:
<code>Hello from main thread
Hello from new thread
</code>
I would expect the output to be:
<code>Hello from new thread
Hello from main thread
</code>
Why is the output not what I expect?


A:

The order of execution is not guaranteed.
The main thread is the one that starts the program. The main thread creates a new thread, and then the two threads run in parallel.
The main thread and the new thread are both executing the same code, but they are not executing it at the same time.
The main thread runs the first line of code, and then the new thread runs the first line of code. Then the main thread runs the second line of code, and then the new thread runs the second line of code.
The main thread and the new thread are both running the same code,
