import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(map(str, range(100000)))))
</code>
to see if it's possible to make a thread that has a very large stack.
The result is that the thread is created but the output is not printed.
I tried to run the code in a terminal and in a notebook, but the result is the same.
I also tried to increase the stack size with <code>threading.stack_size(2**27)</code> but it didn't work.
Is it possible to make a thread with a very large stack?
If so, how?
If not, why?

