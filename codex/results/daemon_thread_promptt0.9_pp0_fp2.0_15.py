import threading
# Test threading daemon
# http://qiita.com/jyori112/items/f099b9bf3c2c44d48a0a

class MyThread(threading.Thread):
    def __init__(self, event):
        threading.Thread.__init__(self)
        self.stopped = event

    def run(self):
        while not self.stopped.wait(1):
            print 'mythread running...'

stopFlag = threading.Event()
thread = MyThread(stopFlag)
thread.start()



Button(root, text='stop', command=stopFlag.set).pack()
Button(root, text='resume', command=stopFlag.clear).pack()

root.mainloop()



import threading
import Queue

# Some things to send to the thread
numlist = range(10)
strlist = 'Hello World!'

# Create a queue
q = Queue.Queue()

def fun(q, strlist, numlist):
    # Put some values into the queue
    for strr in strlist:

