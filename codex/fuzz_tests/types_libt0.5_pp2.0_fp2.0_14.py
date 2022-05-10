import types
types.new_class("foo", object)

class foo(object):
    def __init__(self):
        self.a = 'a'
        self.b = 'b'

def test_get_members():
    assert get_members(foo()) == ['a', 'b']

def test_get_members_with_inheritance():
    class bar(foo):
        def __init__(self):
            self.c = 'c'
            super(bar, self).__init__()
    assert get_members(bar()) == ['a', 'b', 'c']

def test_get_members_with_inheritance_and_override():
    class bar(foo):
        def __init__(self):
            self.a = 'x'
            super(bar, self).__init__()
    assert get_members(bar()) == ['a', 'b']

def test_get_members_with_inheritance_and_override_and_super():
    class bar(foo):
        def __init__(self):
            self.
