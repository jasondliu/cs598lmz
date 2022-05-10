import threading
# Test threading daemon 

def do_this(name):
    while True:
        time.sleep(1)
        print("Thread %s running" %name)

def main():
    for i in range(5):
        t = threading.Thread(target=do_this, args=(i,))
        t.setDaemon(True)
        t.start()

    print("Main thread finishing")

if __name__=="__main__":
    main()


# Joining a Thread 
# Important: Threads do not share global variables, so in this example
# the variable n will be different from the main thread
import time
import threading

def do_this(name):
    time.sleep(1)
    print("Thread %s starting" %name)
    time.sleep(1)
    print("Thread %s finishing" %name)

def main():
    t = threading.Thread(target=do_this, args=(1,))
    t2 = threading.Thread(target=do_this, args=(2,))
    t3 = threading.Thread
