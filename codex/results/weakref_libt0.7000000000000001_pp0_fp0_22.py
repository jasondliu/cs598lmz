import weakref

class MonitoredDict(Collections.MutableMapping):
    '''
    A dictionary that allows other objects to be notified if any changes occur.
    Unlike native dictionaries, this does not allow setting items to None.
    '''

    def __init__(self, *args, **kwargs):
        self.__dict = dict(*args, **kwargs)
        self.__weakref = weakref.WeakSet()

    def __getitem__(self, key):
        return self.__dict[key]

    def __setitem__(self, key, value):
        if value is None:
            raise ValueError('This dictionary does not allow setting any items to None.')
        if key in self.__dict and self.__dict[key] is value:
            return
        self.__dict[key] = value
        for callback in self.__weakref:
            callback()

    def __delitem__(self, key):
        del self.__dict[key]
        for callback in self.__weakref:
            callback()

    def __iter__(
