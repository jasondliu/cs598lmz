gi = (i for i in ())
# Test gi.gi_code


class C:
    def __init__(self, x):
        self.x = x

    def __iter__(self):
        yield self.x


c = C(1)
ci = c.__iter__()
# Test ci.gi_frame


class C:
    def __init__(self, x):
        self.x = x

    def __iter__(self):
        yield self.x
        yield self.x + 1


c = C(1)
ci = c.__iter__()
# Test ci.gi_running


class C:
    def __init__(self, x):
        self.x = x

    def __iter__(self):
        yield self.x


c = C(1)
ci = c.__iter__()
# Test ci.gi_yieldfrom


class C:
    def __init__(self, x):
        self.x = x

    def __iter__(self):
        yield self.x


c = C(1)
ci = c.__iter
