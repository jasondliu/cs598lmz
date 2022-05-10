import threading
# Test threading daemon threading
import time

def hello(name):
    time.sleep(1)
    print("Hello " + name)

t1 = threading.Thread(target=hello, args=('Alice',))
print("Starting thread...")
t1.start()
t2 = threading.Thread()
print("Not starting thread...")
print("End!")
