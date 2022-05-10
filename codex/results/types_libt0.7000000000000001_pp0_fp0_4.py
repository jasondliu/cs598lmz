import types
types.MethodType

def put_count(self):
    self.count = self.count + 1

def put_count2(self, y):
    self.count = y + 1

def put_count3(self):
    self.count = self.count + 1

def put_count4(self, y):
    self.count = y + 1

def put_count5(self, arg):
    self.count = arg

def put_count6(self, arg):
    if arg == None:
        self.count = self.count + 1
    else:
        self.count = arg

class A:
    def __init__(self):
        self.count = 0

a = A()

a.inc = types.MethodType(put_count, a)
a.inc()
assert a.count == 1

a.inc = types.MethodType(put_count2, a)
a.inc(0)
assert a.count == 1

a.inc = types.MethodType(put_count3, a)
a.inc
