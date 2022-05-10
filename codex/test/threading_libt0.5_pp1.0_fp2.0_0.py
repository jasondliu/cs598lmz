import threading
threading.stack_size(67108864)

def func():
    print("thread")

t = threading.Thread(target=func)
t.start()
t.join()
