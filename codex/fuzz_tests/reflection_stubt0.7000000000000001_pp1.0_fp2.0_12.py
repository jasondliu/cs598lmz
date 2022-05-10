fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #27582: Segfault when resizing list in list.__iadd__
class Dummy(object):
    """Used for testing interaction between __iadd__ and __del__
    """
    def __iadd__(self, other):
        other += [1]
        return other
    def __del__(self):
        pass

class Dummy2(object):
    def __iadd__(self, other):
        other += [1]
        return other

class Dummy3(object):
    def __init__(self):
        self.dummy = Dummy()
    def __del__(self):
        del self.dummy

class Dummy4(object):
    def __init__(self):
        self.dummy = Dummy2()
    def __del__(self):
        del self.dummy

dummy = Dummy3()
l = [dummy]
l += l

dummy = Dummy4()
l = [dummy]
l += l

# Issue #27
