import _struct
import _random
import _imp

def _test():
    import sys

    # Sample code to test the module
    print("testing _thread")
    print("CPU count:", _thread.get_count())

    lock = _thread.allocate_lock()
    print("acquire lock...",)
    sys.stdout.flush()
    lock.acquire()
    print("...acquired")
    print("acquire lock again...",)
    sys.stdout.flush()
    lock.acquire()
    print("...acquired")

    def worker():
        print("acquire lock in worker...",)
        sys.stdout.flush()
        lock.acquire()
        print("...acquired")
        print("release lock in worker...",)
        sys.stdout.flush()
        lock.release()
        print("...released")

    print("start new thread")
    _thread.start_new_thread(worker, ())
    while lock.locked():
        pass
    print("lock is not acquired by thread")

    print("release lock...",)
    sys
