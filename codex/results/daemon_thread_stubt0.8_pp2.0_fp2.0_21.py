import sys, threading

def run():
    while True:
        pass

class Thread(threading.Thread):
    def __init__(self,*args,**kwargs):
        super(Thread,self).__init__(*args,**kwargs)
        self.daemon=True
        self.start()
    def run(self):
        while True:
            pass

for i in range(1000):
    Thread()

print threading.active_count()
import threading

def show(x):
    print x

t = threading.Timer(1.0, show, ["Hello World"])
t.start()
t.cancel()
import threading

class MyThread(threading.Thread):

    def run(self):
        print "Hello World!"


# MyThread().start()
MyThread().run()
import threading

class MyThread(threading.Thread):

    def __init__(self,name,id):
        self.name = name
        self.id = id
        threading.Thread.__init__(self)

    def run(self):

