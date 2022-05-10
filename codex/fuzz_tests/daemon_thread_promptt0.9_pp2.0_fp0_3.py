import threading
# Test threading daemon
#https://bradmontgomery.net/blog/understanding-pythons-gil/

def do_something(args):
    for i in range(args[1]):
        print(args[0],threading.current_thread().getName())
        time.sleep(0.1)


x = "hello world"
i = 0
d = True

def loop():
    global i
    while d:
        print(x)
        time.sleep(0.1)
        i += 1
        if i>10:
            break
        #Threading
        t = threading.Thread(target=do_something,args=["Hi",10],)
        t.start()

t2 = threading.Thread(target=loop)
t2.start()
