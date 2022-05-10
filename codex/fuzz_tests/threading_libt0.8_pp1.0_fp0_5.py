import threading
threading.stack_size(67108864)

def func() :
    for i in range(500000) :
        print (i)
        
t = threading.Thread(target=func)
t.start()
t.join()
