import gc, weakref


def dict_subkey(d, *keys):
    """
    Returns a value by tuple of *keys in a nested dictionary.
    If any of *keys are not found, an exception is raised.
    If a list or tuple is passed, the value is returned directly.
    """
    if isinstance(d, (list, tuple, set)):
        return d
    elif isinstance(d, dict) and keys:
        return dict_subkey(d[keys[0]], *keys[1:])
    return d


class lock_key(object):
    """
    A context manager that handles acquiring and releasing a lock
    and allows for passing a defined key for the lock.
    """
    def __init__(self, lock, key):
        self.lock = lock
        self.key = key

    def __enter__(self):
        self.lock.acquire(self.key)

    def __exit__(self, typ, val, traceback):
        self.lock.release(self.key)


