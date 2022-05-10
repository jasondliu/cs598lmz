import threading
# Test threading daemonize mode with I/O
def run():
    for i in range(1):
        print("Name and type of thread is {x}.\
              Thread number is {y}".format(x=threading.currentThread().getName(), y=threading.activeCount()))
        if threading.currentThread().getName() == "Thread-1":
     
