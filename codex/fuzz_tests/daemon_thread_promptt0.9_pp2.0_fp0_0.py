import threading
# Test threading daemonicity

def func1(name):
    print("func1 says: {}".format(name))
    threading.Event().wait(5)

tmp = threading.Thread(target=func1, args=("Hello World!",))
tmp.daemon = False
tmp.start()
print("main thread sleeps")
#threading.Event().wait(10)
time.sleep(5)
print("main thread terminates")

def func2():
    print("func2 says: Why I am not running?")
    threading.Event().wait(5)
tmp = threading.Thread(target=func2, args=())
tmp.daemon = True
tmp.start()
print("Exiting")

while True:
    time.sleep(1)
