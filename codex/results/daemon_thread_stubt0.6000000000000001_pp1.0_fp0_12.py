import sys, threading

def run():
    while True:
        x = input()
        print(x)

threading.Thread(target=run).start()

while True:
    print('hello')
    time.sleep(1)
</code>
How can I get the output of <code>x = input()</code> in the main thread?


A:

You can use <code>multiprocessing.Queue</code>.
<code>from multiprocessing import Process, Queue
from time import sleep

def run(q):
    while True:
        x = input()
        q.put(x)

q = Queue()
p = Process(target=run, args=(q,))
p.start()

while True:
    print('hello')
    sleep(1)
    if not q.empty():
        print(q.get())
</code>

