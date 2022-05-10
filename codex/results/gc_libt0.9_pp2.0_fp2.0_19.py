import gc, weakref
import logging


__all__ = ['ThreadLocalBase', 'ThreadLocalProxy', 'ThreadLocal']



builder_registry = weakref.WeakKeyDictionary()


def cleanup_thread_local(self):
    del self.__dict__['__storage__']


class ThreadLocalProxy(object):

    __slots__ = '__subject__'

    def __init__(self, subject):
        self.__subject__ = subject

    def __getattribute__(self, name):
        subject = super(ThreadLocalProxy, self).__getattribute__('__subject__')
        return getattr(subject, name)


class ThreadLocalBase(object):
    """
    This is a generic class to hold the thread local values. Derived
    classes, written in C or deriving ThreadLocalProxy, can be used
    use it to store their internal thread local state.
    """

    __slots__ = ('__dict__', '__storage__', '__builder__')

    def __init__(self, builder = None):
        object.__setattr__(self, '__
