import sys, threading

def run():
    sys.stdout.write('Running\n')

thread = threading.Thread(target=run)
thread.start()
</code>
This returns:
<code>Running
</code>
Why is the script not waiting until the thread is finished?


A:

You should call the <code>thread.join()</code> method:
<code>import sys, threading

def run():
    sys.stdout.write('Running\n')

thread = threading.Thread(target=run)
thread.start()
thread.join()
</code>

