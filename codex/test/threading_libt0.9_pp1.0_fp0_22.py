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
