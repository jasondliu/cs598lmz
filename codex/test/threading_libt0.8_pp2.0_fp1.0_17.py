import threading
threading.stack_size(64*1024)

def f(name):
    print('hello threading',name)

t = threading.Thread(target=f,args=(5,))
t.start()
