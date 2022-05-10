import sys, threading

def run():
    lock.acquire()
    print('Invoked')
    sys.exit()

threads = []

for x in range(10):
    lock = threading.Lock()
    t = threading.Thread(target=run)
    t.start()
    threads.append(t)

for t in threads:
    t.join()
</code>
I have a lock in the run function and I acquire that lock.
How is it that all threads are able to enter the run function? I thought only one thread at a time can have the lock and thus, only one thread at a time can enter the run function.
I would appreciate any help.
Thanks.


A:

<code>for x in range(10):
    lock = threading.Lock()
    t = threading.Thread(target=run)
    t.start()
    threads.append(t)
</code>
The problem is that you are creating a new lock for each thread you create.  You need to create the lock once before the for-loop.

