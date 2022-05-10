fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
b = fn()


class C:
    def __init__(self):
        self.a = 1

    def __eq__(self, other):
        return self.a == other.a

    def __ne__(self, other):
        return self.a != other.a

    def __lt__(self, other):
        return self.a < other.a

    def __le__(self, other):
        return self.a <= other.a

    def __gt__(self, other):
        return self.a > other.a

    def __ge__(self, other):
        return self.a >= other.a


a = C()
b = C()
a == b
a != b
a < b
a <= b
a > b
a >= b


class C:
    def __init__(self):
        self.a = 1

    def __setitem__(self, key, value):
        pass

    def __delitem__(self, key):
        pass

    def __getitem__(self, key):

