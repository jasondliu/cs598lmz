import sys, threading

def run():
    for i in range(100):
        a = i
        if (a == 100):
            sys.exit()

threading.Thread(target=run).start()

for i in range(100):
    print(i)
</code>
When I run this, it prints numbers from 0 to 99, and then it hangs.
However, when I remove the <code>sys.exit()</code> line, the program prints numbers from 0 to 99, and then it prints numbers from 0 to 99 again, as expected.
What I want is that the program prints numbers from 0 to 99, and then it exits.
I tried to use <code>sys.exit()</code> in the main thread as well, but it had no effect.
How can I make the program exit after printing numbers from 0 to 99?


A:

<code>sys.exit()</code> does not kill the program. It raises the <code>SystemExit</code> exception, which will be caught by the <code>run()</code> function, and then the program will continue to run.
You need to raise the exception in the main thread
