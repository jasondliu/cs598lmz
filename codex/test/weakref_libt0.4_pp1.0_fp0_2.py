import weakref

from . import _utils
from . import _compat
from . import _compat_collections


class _DummyLock(object):
    """
    Dummy lock class.
    """
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        pass


class _DummyLockManager(object):
    """
    Dummy lock manager class.
    """
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def __call__(self, *args, **kwargs):
        return _DummyLock()


class _DummyLockContext(object):
    """
    Dummy lock context class.
    """
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def __call__(self, *args, **kwargs):
        return self


