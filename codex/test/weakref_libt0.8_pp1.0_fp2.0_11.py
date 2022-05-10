import weakref

class Funct(object):
    """
    Return a function with a specific signature (the arglist)
    """
    def __init__(self, length, func, arglist):
        self.length = length
        self.func = func
        self.arglist = arglist

    def __call__(self, *args):
        if len(args) != self.length:
            raise TypeError(
                "__call__() takes exactly %d arguments (%d given)" % (
                self.length, len(args) + 1))
        return self.func(*args, **dict(zip(self.arglist, args)))


class CmdSet(object):
    """
    A set of commands. This is a group of commands that should
    be treated as a unit when being added or removed from the
    command handler.

    Note that order does matter, so don't use sets. The cmdset
    is checked for matching commands by starting from the last
    command added to the cmdset.
    """

