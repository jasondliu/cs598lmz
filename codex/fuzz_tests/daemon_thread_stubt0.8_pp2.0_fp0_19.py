import sys, threading

def run():
    while True:
        threading.Thread(target=time.sleep, args=(1,)).start()

run()
print(threading.activeCount())
</code>
I was expecting that after a few seconds the thread count would be much higher than it is, so I must be missing something.
I tried running the script with python 2.7 and 3.6 with the same results.


A:

Threading is a funny thing. It creates threads which are system processes running in the background, consuming system resources. The python's threading module also uses a thread pool even when you use <code>threading.Thread</code>.
The <code>threading.activeCount()</code> function returns the number of active threads in the pool. When a thread finishes execution, it is returned to the pool. This is why your code will never print a value above 10.
Also, The <code>threading.Thread</code> is an abstraction of the Thread class which in-turn creates and starts a new thread by calling the <code>run()</code> method. We could just as easily call the <code>threading.Thread(target = time
