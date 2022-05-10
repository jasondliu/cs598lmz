from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __dict__

class C(object):
    def __init__(self, x):
        self.x = x

c = C(10)
c.__dict__

c.y = 20
c.__dict__

c.__dict__['z'] = 30
c.__dict__

c.__dict__['x'] = 40
c.__dict__

c.x

# __slots__

class C(object):
    __slots__ = ['x']
    def __init__(self, x):
        self.x = x

c = C(10)
c.__dict__

c.y = 20
c.__dict__

c.__dict__['z'] = 30
c.__dict__

c.__dict__['x'] = 40
c.__dict__

c.x

# __getattribute__

