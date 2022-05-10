import sys, threading

def run():
    sys.stdout.write('Hello from thread %s\n' % threading.currentThread())

def test():
    for i in range(5):
        t = threading.Thread(target=run)
        t.start()

if __name__ == "__main__":
    test()
</code>
The output is:
<code>Hello from thread &lt;_MainThread(MainThread, started 140735330039296)&gt;
Hello from thread &lt;Thread(Thread-1, started 140735330039296)&gt;
Hello from thread &lt;Thread(Thread-2, started 140735330039296)&gt;
Hello from thread &lt;Thread(Thread-3, started 140735330039296)&gt;
Hello from thread &lt;Thread(Thread-4, started 140735330039296)&gt;
Hello from thread &lt;Thread(Thread-5, started 140735330039296)&gt;
</code>
Why is <code>MainThread</code> started in <code>
