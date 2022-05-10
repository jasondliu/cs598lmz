import sys, threading

def run():
    print "running"
    sys.stdout.flush()
    threading.Event().wait(10)
    print "done"
    sys.stdout.flush()

thread = threading.Thread(target=run)
thread.start()
thread.join()
</code>
Output:
<code>running
done
</code>

