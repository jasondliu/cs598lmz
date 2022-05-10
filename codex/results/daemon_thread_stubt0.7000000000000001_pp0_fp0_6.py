import sys, threading

def run():
    for i in range(100):
        print(i)
        time.sleep(1)

t = threading.Thread(target=run)
t.start()

stdin = sys.stdin.readline().strip()
print(stdin)
print(sys.stdin)
</code>
So my question is, why can it get the input "a", but not "b"?
I am using Python 3.7.2.


A:

I ran your code in another terminal, and it worked fine.
I think it's because in your terminal, you have an <code>echo</code> that is enabled by default.
If you type something, it will echo back to you.
So the first time, you type <code>a</code>, it echoes back to you, and then the <code>sys.stdin.readline()</code> captures the <code>a\n</code> (the \n is for end of line)
The second time, you type b, and it echoes back to you, but <code>sys.stdin.readline()</code> is already waiting
