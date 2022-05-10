import selectors
import sys
from datetime import datetime
import time
import os
from Queue import Queue

#import threading
from threading import current_thread, Thread


def thread_message(tid,q):
    #tid=threading.currentThread()
    while 1:
        print("第",tid,"个线程输出")
        infor=q.get(1)
        print(infor)
        time.sleep(1)
#    print(tid)
#    print(currentThread())

def get_thread_name():
    thread_name=threading.current_thread().getName()
    print(thread_name)

def main_func():
    threads=[]
    q=Queue()
    t1=Thread(target=thread_message,args=(1,q))
    t2=Thread(target=thread_message,args=(2,q))
    t1.start()
    t2.start()
    q.put((1,2,3,4,5))
