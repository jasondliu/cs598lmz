import sys, threading

def run():
    while 1:
        print "hello"
        time.sleep(1)

class MyThread(threading.Thread):
    def run(self):
        while 1:
            print "hello"
            time.sleep(1)

t = MyThread()
t.start()

while 1:
    print "world"
    time.sleep(1)
