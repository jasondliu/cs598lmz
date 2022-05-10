import sys, threading

def run():
    while 1:
        print "thread"
        time.sleep(1)

def main():
    thread = threading.Thread(target=run, args=(), name="thread")
    thread.daemon = True
    thread.start()
    while 1:
        print "main"
        time.sleep(1)

if __name__ == "__main__":
    main()
</code>
When I run the program, only <code>main</code> is printed and the thread is not executed. If I remove <code>thread.daemon = True</code>, the thread is executed and I can see the <code>thread</code> and <code>main</code> strings being printed.
Why does setting <code>daemon</code> to <code>True</code> prevent the thread from running?


A:

From the documentation:
<blockquote>
<p>A thread can be flagged as a “daemon thread”. The significance of this flag is that the entire Python program exits when only daemon threads are left.</p>
</blockquote>
What is happening is that
