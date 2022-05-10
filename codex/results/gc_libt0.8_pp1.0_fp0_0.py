import gc, weakref
import bisect

def stopwatch(message, func, *args, **kwds):
    t1 = time.time()
    result = func(*args, **kwds)
    print(message, time.time() - t1)
    return result

class TimeoutError(Exception):
    pass

def timeout(func, secs=15, force_kill=False, *args, **kwds):
    def timeout_handler(signum, frame):
        msg = 'timed out after %.3f seconds' % secs
        raise TimeoutError(msg)
    
    old = signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(secs)
    try:
        result = func(*args, **kwds)
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, old)
    
    return resu

def memory(message, func, *args, **kwds):
    gc.collect()
    before = gc.mem_free
