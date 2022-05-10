import threading
# Test threading daemon
#

# If a thread is set as daemon, it will automatically exit when the parent thread exits
class ThreadFunc(object):
    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):
        apply(self.func, self.args)

def loop_print(nloop, nsec):
    print('start loop', nloop, 'at', ctime())
    sleep(nsec)
    print('loop', nloop, 'done at', ctime())

def main():
    print('starting at:', ctime())

    threads = []
    nloops = range(len(loops))
    # loop_print(nloops[0], loops[0])
    # loop_print(nloops[1], loops[1])
    # loop_print(nloops[2], loops[2])
    # loop_print(nloops[3], loops[3])
    # loop_print(nloops[4],
