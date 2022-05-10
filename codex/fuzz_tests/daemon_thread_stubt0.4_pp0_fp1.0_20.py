import sys, threading

def run():
    while True:
        print('thread running')
        time.sleep(1)

t = threading.Thread(target=run)
t.start()

while True:
    print('main thread running')
    time.sleep(1)
</code>
I expect that the program will print <code>thread running</code> and <code>main thread running</code> every second, but it prints only <code>main thread running</code> every second.
I use python 3.7.3 on Ubuntu 18.04.
What am I doing wrong?


A:

You're not doing anything wrong, it's just that the output is buffered and not flushed to the console.
If you add a <code>flush=True</code> argument to the <code>print</code> function, you'll see the desired output:
<code>import time, sys, threading

def run():
    while True:
        print('thread running', flush=True)
        time.sleep(1)

t = threading.Thread(target=run)
t.start()

while True:

