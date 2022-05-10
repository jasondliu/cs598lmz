import sys, threading

def run():
    print("run")
    sys.exit()

thread = threading.Thread(target=run)
thread.start()

print("main")
</code>
The output is:
<code>run
main
</code>
I would like to have the output:
<code>main
run
</code>
How can I do that?


A:

You can't. The thread is started in the background, and the main thread continues to run.
If you want to wait for the thread to finish, you can use <code>thread.join()</code>.

