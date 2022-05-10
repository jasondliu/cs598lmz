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
