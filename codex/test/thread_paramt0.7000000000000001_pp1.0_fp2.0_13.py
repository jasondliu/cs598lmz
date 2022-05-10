import sys, threading
threading.Thread(target=lambda: sys.stdout.write('hello world\n')).start()

#
import threading

class ThreadFunc(object):
    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):
        self.func(*self.args)

def loop(nloop, nsec):
    print('start loop {} at:'.format(nloop), ctime())
    sleep(nsec)
    print('loop {} done at: '.format(nloop), ctime())

def main():
    print('starting at: ', ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(
            target=ThreadFunc(loop, (i, loops[i]), loop.__name__))
        threads.append(t)

    for i in nloops:
        threads[i].start()

