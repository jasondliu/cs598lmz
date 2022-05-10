import threading
threading.stack_size(1000000000)

def m(l):
    l = [i+i for i in l]
    return l

l = range(5000000)
t1 = threading.Thread(target=m, args=[l])
t1.start()
t1.join()
t2 = threading.Thread(target=m, args=[l])
t2.start()
t2.join()
print l[1000]
</code>
(Note: I also tried <code>with ThreadPoolExecutor(max_workers=2) as executor:</code> and got same error)
It could be stack size is set just below threshold (stack size is important since Python interpreter is written in C and C is not GCed), so I wonder how to set stack size even larger? I guess stack size is set by ulimit? But my ulimit -s is unlimited, so I don't understand how to set it higher.
OS is Ubuntu 14.04
Thank you.

