import sys, threading

def run(): 
    while True:
        print "Thread 1"

def run2(): 
    while True:
        print "Thread 2"

threads = []
t = threading.Thread(target=run)
threads.append(t)
t.start()

t = threading.Thread(target=run2)
threads.append(t)
t.start()
</code>
and here is the output:
<code>$ python t.py
Thread 1
Thread 1
Thread 1
Thread 1
Thread 1
Thread 1
Thread 1
Thread 1
Thread 1
Thread 1
Thread 1
Thread 1
Thread 1
Thread 1
Thread 1
Thread 1
Thread 1
Thread 1
Thread 1
Thread 1
Thread 1
Thread 1
Thread 1
Thread 1
Thread 1
Thread 1
Thread 1
Thread 1
Thread 1
Thread 1
Thread 1
Thread 1
Thread 1
Thread 1
Thread 1
Thread 1
Thread 1
Thread 1
Thread 1
Thread 1
Thread 1
Thread 1
Thread 1
Thread 1
Thread 1
Thread 1
Thread 1
Thread 1
Thread
