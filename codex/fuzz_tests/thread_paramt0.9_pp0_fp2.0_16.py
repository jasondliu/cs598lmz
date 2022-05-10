import sys, threading
threading.Thread(target=lambda: sys.stdout.write("Goodbye")).start()

#Q2:
import threading
import time
def printt(x):
    while x > 0:
        print("Hallo")
        x=x-1
        time.sleep(1)

threading.Thread(target=printt, args=(10,)).start()

#Q3:
import threading
from queue import Queue
def counter (x):
    for i in range(0,x):
        print(i)
        time.sleep(1)

def counter2 (x):
    for i in range(x,x+x):
        print(i)
        time.sleep(1)

threads = []

t1 = threading.Thread(target=counter,args=(5,))
t2 = threading.Thread(target=counter2,args=(5,))

threads.extend((t1,t2))

t1.start()
t2.start()
t1.join()
t2.join()


#Q4:
import thread
