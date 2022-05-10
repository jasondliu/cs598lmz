import sys, threading

def run():
    print("Hello from thread %s" % threading.current_thread())

def main():
    print("Hello from thread %s" % threading.current_thread())
    for i in range(5):
        t = threading.Thread(target=run)
        t.start()

if __name__ == '__main__':
    main()
</code>
Output:
<code>Hello from thread &lt;_MainThread(MainThread, started 140735442475776)&gt;
Hello from thread &lt;Thread(Thread-1, started 140735442475776)&gt;
Hello from thread &lt;Thread(Thread-2, started 140735442475776)&gt;
Hello from thread &lt;Thread(Thread-3, started 140735442475776)&gt;
Hello from thread &lt;Thread(Thread-4, started 140735442475776)&gt;
Hello from thread &lt;Thread(Thread-5, started 140735442475776)&gt;
</code>

