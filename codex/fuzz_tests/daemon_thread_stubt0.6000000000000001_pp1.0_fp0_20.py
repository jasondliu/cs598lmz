import sys, threading

def run():
    for i in range(0,10):
        print(i)
        time.sleep(1)

def main():
    th = threading.Thread(target=run, args=())
    th.start()
    x = input('Enter Something: ')
    print(x)

if __name__ == '__main__':
    main()
</code>


A:

You can use a <code>queue</code> and have the thread check the <code>queue</code> for data to get the input:
<code>import time
import sys
import threading
import queue
import tkinter as tk

def run(q):
    for i in range(0,10):
        print(i)
        time.sleep(1)
    try:
        q.get(block=False)
    except queue.Empty:
        pass

def main():
    q = queue.Queue()
    th = threading.Thread(target=run, args=(q,))
    th.start()
    root = tk.Tk()
    e
