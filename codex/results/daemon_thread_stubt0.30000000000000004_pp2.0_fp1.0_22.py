import sys, threading

def run():
    print("run")
    sys.exit()

t = threading.Thread(target=run)
t.start()

while True:
    print("main")
    time.sleep(1)
</code>
I expected the output to be:
<code>run
main
main
main
main
main
</code>
But I got:
<code>run
</code>
Why is this happening?


A:

<code>sys.exit()</code> will exit the entire process.
If you want to exit the thread, use <code>threading.Thread.exit()</code> instead.

