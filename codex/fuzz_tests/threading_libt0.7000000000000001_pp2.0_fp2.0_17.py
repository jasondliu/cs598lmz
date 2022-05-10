import threading
threading.Thread(target=go, args=(x,x)).start()
</code>
I was thinking to add a lock on the go function, but I have several go functions, and all other threads need to execute the go functions in parallel.


A:

You can use the <code>threading.Lock</code>.
<code>lock = threading.Lock()

def go(x):
    lock.acquire()
    try:
        global a
        a = x
        print(a)
    finally:
        lock.release()

threading.Thread(target=go, args=(x,x)).start()
</code>
Note: When you use a lock, you have to <code>acquire</code> it before changing the variable and <code>release</code> it as soon as you no longer need to change the variable. Because other <code>Threads</code> that aren't <code>running</code> won't be able to change the variable until you <code>release</code> the lock.

