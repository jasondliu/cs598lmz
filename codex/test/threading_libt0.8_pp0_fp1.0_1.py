import threading
threading.current_thread()


import sys
import thread

#Threaded Function
def print_a():
    for n in range(1,6):
        print ("A:%s\n" % n)

def print_b():
    for n in range(1,6):
         print ("B:%s\n" % n)

#Create Threads
