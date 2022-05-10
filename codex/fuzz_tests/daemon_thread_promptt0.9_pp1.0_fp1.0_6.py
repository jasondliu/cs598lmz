import threading
# Test threading daemon

def hello(name):
    for i in range(0,10):
        time.sleep(1)
        print "Hello {0}".format(name)

t1 = threading.Thread(target=hello,args=("Kamal",))
t2 = threading.Thread(target=hello,args=("Kumar",))

t1.start()
t2.start()
