import weakref
# Test weakref.ref and weakref.proxy in a multithreaded environment.
# No objects are actually weakly referenced by this test;
# instead, it merely calls random methods of random proxies and confirms
# that there is no segmentation fault.


LEN_ITERATIONS = 1000

NUM_THREADS = 100
NUM_OBJECTS = 100
NUM_CALLS = 100


class MyObject(object):
    pass

objects = [MyObject() for i in range(NUM_OBJECTS)]


def worker(wid, queue):
    while True:
        while queue.empty():
            continue
        obj = queue.get()
        if obj is None:
            return
        r = weakref.ref(obj)
        del r
        p = weakref.proxy(obj)
        del p
        calls = [getattr(obj, attr) for attr in dir(obj)
                 if not attr.startswith('_')]
        calls = [random.choice(calls) for i in range(NUM_CALLS)]
        for func in calls:

