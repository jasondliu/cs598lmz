import sys, threading
threading.Thread(target=lambda: sys.stdout.write('thread')).start()
</code>
The output is:
<code>threadmain
</code>
I would like to know why is this happening?


A:

This is because <code>sys.stdout.write</code> is a blocking operation.
The <code>print</code> function is not, however.
<code>def print_thread():
    print('thread')

threading.Thread(target=print_thread).start()
print('main')
</code>
This will output
<code>main
thread
</code>

