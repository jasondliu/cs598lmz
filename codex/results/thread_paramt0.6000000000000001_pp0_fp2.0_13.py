import sys, threading
threading.Thread(target=lambda: sys.stdout.write('a')).start()
threading.Thread(target=lambda: sys.stdout.write('b')).start()
</code>
This is the output:
<code>ba
</code>
I don't understand why it is not <code>ab</code>. 
The output is different every time I run it. 
How can I make the output always be <code>ab</code>? 
And why is it not <code>ab</code>?


A:

What you get is pretty much random. The reason is that there is nothing to happen in between the <code>start</code> and the actual <code>sys.stdout.write</code> call. I.e. the <code>start</code> method will just start the thread and then continue with the next statement.
You can see this with the following code:
<code>import sys, threading

def print_a():
    sys.stdout.write('a')

def print_b():
    sys.stdout.write('b')

threading.Thread(target=print
