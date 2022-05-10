import gc, weakref, sys, threading

class Stack(list):
    def push(self, item):
        self.append(item)

    def pop(self, item):
        self.remove(item)

_weakref = weakref.ref
_stack = Stack()
_finalizer_lock = threading.Lock()
_shutdown = False

def finalize(object, callback, *args, **kwargs):
    if _shutdown:
        raise RuntimeError('cannot register finalizer during shutdown')
    assert callable(callback), 'callback is not callable'
    _finalizer_lock.acquire()
    try:
        finalizer = _Finalizer(object, callback, args, kwargs)
        _stack.push(finalizer)
    finally:
        _finalizer_lock.release()

def _run_finalizers():
    while _stack:
        finalizer = _stack.pop()
        try:
            finalizer()
        except:
            pass

class _Finalizer:
    def __init__(self, object, callback, args, k
