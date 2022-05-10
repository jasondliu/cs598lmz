import sys, threading

def run():
    while True:
        sys.stdout.write('\x1b[2J\x1b[H')
        print(threading.enumerate())
        time.sleep(0.5)

t = threading.Thread(target=run)
t.start()

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

while True:
    print(add(1, 2))
    print(sub(3, 4))
    time.sleep(0.5)
</code>
Output:
<code>[&lt;_MainThread(MainThread, started 140734385724224)&gt;, &lt;Thread(Thread-1, started daemon 140705745288960)&gt;, &lt;Timer(Thread-2, started daemon 140705745288704)&gt;]
3
-1
[&lt;_MainThread(MainThread, started 140734385724224)&gt;, &lt;Thread(Thread-1, started daemon 140705745
