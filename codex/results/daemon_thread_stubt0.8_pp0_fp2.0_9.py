import sys, threading

def run():
    while True:
        if ord(sys.stdin.read(1)) == 3:
            print("kaboom")

threading.Thread(target=run).start()
</code>
I use this to get user input without blocking the loop in my actual program. I then plan to handle the keyboard interrupt separately. However, when I run this code in the interpreter, I get a KeyboardInterrupt (hit by Ctrl+C) error. How do I make this work?


A:

You need to wrap the sys.stdin.read(1) in a try.  When you hit ctrl+c, the main interpreter thread raises the exception KeyBoardInterrupt, but the "run" thread is in the middle of sys.stdin.read(1) ... so the exception is never caught.
<code>import sys, threading

def run():
    while True:
        try:
            if ord(sys.stdin.read(1)) == 3:
                print("kaboom")
        except KeyboardInterrupt:
            print("KeyboardInterrupt caught in run thread")

threading.Thread(target
