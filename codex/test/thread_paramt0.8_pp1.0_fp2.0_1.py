import sys, threading
threading.Thread(target=lambda: sys.stdout.write(input())).start()
threading.Thread(target=lambda: sys.stderr.write(input())).start()
 
#import threading
#threading.Thread(target=(lambda : print(input()))).start()
#threading.Thread(target=(lambda : print(input(), file=sys.stderr))).start()

#from time import time
#from time import sleep
#from random import randint
#from threading import Thread
#
#class myThread (Thread):
#    def __init__(self, name, counter):
#        Thread.__init__(self)
#        self.threadID = counter
#        self.name = name
#        self.counter = counter
#    def run(self):
#        print ("Starting " + self.name)
#        threadLock.acquire()
#        print_time(self.name, self.counter, 3)
#        threadLock.release()
#
#def print_time(threadName, delay, counter):
#    while counter:
#        time.
