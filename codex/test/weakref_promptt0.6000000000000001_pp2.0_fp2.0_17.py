import weakref
# Test weakref.ref.


class C:

    def __init__(self, arg):
        self.arg = arg

    def __repr__(self):
        return 'C(%r)' % self.arg


class D:

    def __init__(self, arg):
        self.arg = arg

    def __repr__(self):
        return 'D(%r)' % self.arg

    def __hash__(self):
        return hash(self.arg)

    def __eq__(self, other):
        return isinstance(other, D) and self.arg == other.arg


class E:

    def __init__(self, arg):
        self.arg = arg

    def __repr__(self):
        return 'E(%r)' % self.arg

    def __hash__(self):
        return hash(self.arg)

    def __eq__(self, other):
        return isinstance(other, E) and self.arg == other.arg

    def __call__(self, *args):
        return args


