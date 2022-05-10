import sys, threading

def run():
    while True:
        print("Hello")

t = threading.Thread(target=run)
t.start()

sys.exit()
</code>
This will run the <code>run()</code> function in a separate thread, however, when I exit the program, it will close the thread. I want to close the program, but keep the thread running.
I've tried to use <code>daemon = True</code> but that doesn't seem to work.


A:

You can use the <code>daemon</code> property of a <code>threading.Thread</code> instance.
<code>import sys, threading

def run():
    while True:
        print("Hello")

t = threading.Thread(target=run)
t.daemon = True
t.start()

sys.exit()
</code>

