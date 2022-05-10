import sys, threading

def run():
    for i in range(1000):
        print(i)
    sys.exit(0)

thread = threading.Thread(target=run)
thread.start()
</code>
If I run the above code, I can see that the thread is not terminated after the for loop is over.
How can I stop the thread with the specified exit code?


A:

You should use thread.join. 
<code>thread.join()</code> 
<blockquote>
<p>This waits until the thread terminates.</p>
</blockquote>

