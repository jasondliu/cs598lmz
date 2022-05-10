import _struct
# Test _struct.Struct.format_size()

class A(object):
    def __init__(self, name, arg, value=1, items=None):
        self.name = name
        self.arg = arg
        self.value = value
        if items is not None:
            self.items = items
    def __eq__(self, other):
        return (self.name, self.arg, self.value) == (other.name, other.arg, other.value)
    def __repr__(self):
        return "%s(%r, %r, %r)" % (self.__class__.__name__, self.name, self.arg, self.value)
    def __str__(self):
        return "<A %r %r %r>" % (self.name, self.arg, self.value)

class B(A):
    def __init__(self, *args, **kwargs):
        super(B, self).__init__(*args, **kwargs)
        if self.value == 1:
            self.value = 2

