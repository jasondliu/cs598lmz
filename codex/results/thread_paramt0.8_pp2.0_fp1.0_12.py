import sys, threading
threading.Thread(target=lambda:sys.stdout.write(sys.stdin.read())).start()    
</code>
When I run <code>make</code>, however, I only get the following:
<code>$ make
hello
</code>
<code>world</code> is nowhere to be found. 
I am running the latest version of Python 2.7.8 on Linux.
Why is <code>world</code> not being printed? 


A:

Python flushes its output buffers whenever it hits a newline or the end of the script. You didn't print a newline in the other thread.
If you remove the <code>$</code> before <code>make</code>, you will see that <code>world</code> is printed, but <code>echo</code> doesn't wait for it:
<code>$ cat hello.py 
hello
import sys, threading
threading.Thread(target=lambda:sys.stdout.write(sys.stdin.read())).start()

$ make
hello
world
make: echo: Command not found
make: *** [test] Error 127
