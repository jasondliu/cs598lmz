import sys, threading

def run():
    while True:
        print("hello")

threading.Thread(target=run).start()
</code>
The problem is that the program does not exit, because the thread never ends.
I know that I can use <code>sys.exit()</code> to exit the program, but I would prefer a more elegant solution.
Is there a way to kill the thread when the program exits?


A:

You can set a flag in the main thread and check it in the child thread.
<code>import threading

def run():
    while True:
        print("hello")
        if not run.running:
            break

run.running = True
threading.Thread(target=run).start()
run.running = False
</code>

