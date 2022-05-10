import sys, threading

def run():
    for i in range(100):
        print "running " + str(i)
        time.sleep(2)
        print "done"

t = threading.Thread(target=run)
t.start()

run()
</code>
However, when I run the script above, it first runs the <code>run()</code> method in the main thread, and only then starts the new thread. In other words I get the following output:
<code>running 0
done
running 1
done
</code>
Why is this happening, and how can I fix it?
Thanks in advance.


A:

The program doesn't wait for the thread to start until you call <code>join</code>. So, you need to first start the thread and then call <code>join</code> on it:
<code>t.join()
run()
</code>
But you should instead create the thread first and then run the main thread:
<code>t = threading.Thread(target=run)
t.start()
t.join()
</code>

