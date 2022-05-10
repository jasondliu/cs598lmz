import threading
# Test threading daemon

def worker():
    print("I am a worker")
    return

threads = []

for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start(
</code>
it prints <code>5 times O am a worker</code>


A:

In order to set thread daemon set the following :
<code>import threading
import time

def worker():
    print("I am a worker")
    time.sleep(1)
    print("I am working")
    return

threads = []

for i in range(5):
    t = threading.Thread(target=worker)
    t.setDaemon(True)
    threads.append(t)
    t.start()
</code>
In the above sample code we create 5 threads and set them to daemon. When starting each thread the daemon turns the thread to a daemon thread. 

