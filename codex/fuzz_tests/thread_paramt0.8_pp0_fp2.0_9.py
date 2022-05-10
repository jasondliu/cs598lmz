import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Thread1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Thread2\n')).start()
sys.stdout.write('MainThread\n')
</code>
Output:
<code>Thread1
Thread2
MainThread
</code>
The documentation of the threading module states that the <code>target</code> parameter is the callable to be executed by the thread. 
How does the interpreter know that the output of the <code>target</code> parameter is a <code>print</code> statement? And how does the interpreter know that the <code>sys.stdout.write('MainThread\n')</code> is not a <code>print</code> statement? 


A:

<code>sys.stdout</code> is a <code>file</code>-like object which is assigned the standard output of your program (where it should print by default). <code>sys.stdout.write</code> is a <code>file</code> method. It will print to the standard output.
Source

