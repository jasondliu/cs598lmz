import threading
threading.stack_size(67108864)

def f(n):
    return n**2

def run():
    for i in range(1000000):
        f(i)

t = threading.Thread(target=run)
t.start()

import resource
# Show stack size of current process
print('Maximum stack size:', resource.getrlimit(resource.RLIMIT_STACK)[1])

# What is my current stack size?
# i.e. how much memory does my thread stack have?
print('Stack size (bytes):', resource.getrusage(resource.RUSAGE_SELF).ru_isrss)
</code>
the output is:
<code>Maximum stack size: 67108864
Stack size (bytes): 2048
</code>
why the second number is 2048? I set the stack size to 67108864 bytes. But the second number did't change.


A:

Yes, you have set the stack size to <code>67108864</code> bytes but this is the size of the stack, not the usage. The <code
