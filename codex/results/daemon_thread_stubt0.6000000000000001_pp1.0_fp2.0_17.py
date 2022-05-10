import sys, threading

def run():
    print("hi")
t = threading.Thread(target=run())
t.start()
</code>
the output I get is:
<code>hi
hi
</code>
How can I get the output to be:
<code>hi
</code>
Thanks


A:

You are calling <code>run()</code> in the main thread and passing the result of that call to <code>threading.Thread</code>.
You should be passing <code>run</code> itself to <code>threading.Thread</code>:
<code>t = threading.Thread(target=run)
</code>

