import sys, threading

def run():
    while True:
        print("Hello")

threading.Thread(target=run).start()
</code>
I want to kill this thread by pressing a key. How to do that?
I tried this, but it didn't work:
<code>import sys, threading

def run():
    while True:
        print("Hello")

threading.Thread(target=run).start()

while True:
    input = sys.stdin.read(1)
    if input == 'q':
        break
</code>


A:

As @peterk stated in the comments, you can use a global variable to kill the thread.
<code>import sys, threading

def run():
    global kill
    while True:
        if kill:
            break
        print("Hello")

kill = False
threading.Thread(target=run).start()

while True:
    input = sys.stdin.read(1)
    if input == 'q':
        kill = True
        break
</code>

