import sys, threading

def run():
    global thread
    thread = threading.Thread(target=thread_main)
    thread.start()

def thread_main():
    global thread
    while True:
        if not thread.is_alive():
            break
        time.sleep(1)
        print('thread')

run()
print('main')
</code>
I want to stop the thread when the main program stops.
I tried <code>thread.join()</code> in <code>main()</code>, but it caused the program to hang.


A:

<code>import time
import sys, threading

def run():
    global thread
    thread = threading.Thread(target=thread_main)
    thread.start()

def thread_main():
    global thread
    while True:
        if not thread.is_alive():
            break
        time.sleep(1)
        print('thread')

run()
print('main')
</code>

