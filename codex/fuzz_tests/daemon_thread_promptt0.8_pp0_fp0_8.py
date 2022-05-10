import threading
# Test threading daemon
import queue
ioq = queue.Queue()

def reader(fname):
    with open(fname, 'rt') as fp:
        for line in fp:
            ioq.put(line)

def writer():
    with open('out.txt', 'wt') as fp:
        while True:
            line = ioq.get()
            print('Processed: ', line, file=fp)
            ioq.task_done()

threading.Thread(target=writer).start()
reader('input.txt')
ioq.join()
