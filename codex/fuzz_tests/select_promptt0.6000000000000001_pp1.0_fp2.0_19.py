import select
# Test select.select

import threading
import Queue
import time

inq = Queue.Queue()
outq = Queue.Queue()

def reader(inq, outq):
    while 1:
        print 'reader waiting for input'
        data = inq.get()
        if data is None:
            print 'reader got EOF'
            break
        print 'reader got', data
        outq.put(data)
        print 'reader waiting for output'
        outq.get()
        print 'reader done with', data
    print 'reader exiting'

def writer(outq):
    for i in range(5):
        print 'writer sending', i
        outq.put(i)
        print 'writer waiting for output'
        outq.get()
        print 'writer done with', i
    print 'writer sending EOF'
    outq.put(None)
    print 'writer exiting'

rthread = threading.Thread(target=reader, args=(inq, outq))
wthread = threading.Thread(target=writer, args=(out
