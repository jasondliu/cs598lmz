import sys, threading

def run():
    print("run")
    sys.stdout.flush()

t = threading.Thread(target=run)
t.start()

print("main")
sys.stdout.flush()
</code>
Output:
<code>main
run
</code>
If you want to wait until the thread is finished, use <code>t.join()</code>.

