import sys, threading

def run():
    print("run")
    sys.exit()

t = threading.Thread(target=run)
t.start()
t.join()
print("end")
</code>
This code prints:
<code>run
end
</code>
But I want to print:
<code>end
run
</code>
How can I do this?


A:

You can't. <code>sys.exit()</code> will terminate the entire process, not just the thread.

