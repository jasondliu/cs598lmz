import sys, threading

def run():
    while True:
        print('p')
        time.sleep(1)

def main():
    t = threading.Thread(target=run)
    t.start()
    while True:
        print('m')
        time.sleep(1)

if __name__ == '__main__':
    main()
</code>
I've tried using <code>threading.Thread</code> to create a second thread and run it in the background, but the output is still very much like a single-threaded program.
<code>m
p
m
p
m
p
m
p
m
p
m
p
</code>
Am I creating the thread correctly? If not, what's the correct way to create a thread?


A:

<code>import threading
import time

def run():
    while True:
        print('p')
        time.sleep(1)

def main():
    t = threading.Thread(target=run)
    t.start()
    while True:
        print('m')
        time.sleep(
