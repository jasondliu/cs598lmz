import sys, threading

def run():
    while True:
        print "Hello"

if __name__ == "__main__":
    print "Start"
    t = threading.Thread(target=run)
    t.start()
    print "End"
</code>
However, when I run the script, it just prints "Start" and "End" and exits.
I'm running Python 2.7.3 on Windows 7.
Any ideas?


A:

The main thread exits, so the program exits. If you want the program to keep running, you need to keep the main thread alive.
<code>import sys, threading

def run():
    while True:
        print "Hello"

if __name__ == "__main__":
    print "Start"
    t = threading.Thread(target=run)
    t.start()
    print "End"
    t.join()
</code>

