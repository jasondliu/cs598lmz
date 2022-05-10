import gc, weakref
from guppy import hpy
h = hpy()

def _show_resources():
    import sys

    print "hpy.mem():"
    print h.heap()

def show_resources():
    import multiprocessing
    # note that this limits the runtime for each worker to a second
    p = multiprocessing.Process(target=_show_resources)
    p.daemon = True
    p.start()
    p.join(1)
    if p.is_alive():
        print "Could not join"
        print "Killing hanging process"
        p.terminate()
        p.join()

def _run_gc():
    gc.collect()

def run_gc():
    import multiprocessing
    p = multiprocessing.Process(target=_run_gc)
    p.daemon = True
    p.start()
    p.join(2)
    if p.is_alive():
        print "Could not join"
        print "Killing hanging process"
        p.terminate()
