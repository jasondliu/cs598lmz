import sys, threading

def run():
    while True:
        print("Hello")
        time.sleep(1)

run()
</code>
I have tried threading.Thread and multiprocessing.Process, but the output is the same. 
<code>from threading import Thread

def run():
    while True:
        print("Hello")
        time.sleep(1)

t = Thread(target=run)
t.start()
</code>
and 
<code>from multiprocessing import Process

def run():
    while True:
        print("Hello")
        time.sleep(1)

p = Process(target=run)
p.start()
</code>
I have tried using both <code>run()</code> and <code>run()</code> in the <code>if __name__ == '__main__'</code> block. 
I have tried running the code in Python 2.7 and Python 3.5. 
I have tried running the code in PyCharm and in the command line. 
I have tried running the code on Windows 10 and Ubuntu 16.04
