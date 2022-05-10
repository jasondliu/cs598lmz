fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# issue #18
def f():
    return lambda: None

def g():
    return f()

g()()

# issue #19
class A:
    def __init__(self):
        self.x = 1

class B(A):
    def __init__(self):
        super().__init__()

B()

# issue #20
class A:
    def __init__(self):
        self.x = 1

class B(A):
    def __init__(self):
        super(B, self).__init__()

B()

# issue #21
class A:
    def __init__(self):
        self.x = 1

class B(A):
    def __init__(self):
        super(B, self).__init__()

class C(B):
    def __init__(self):
        super(C, self).__init__()

C()

# issue #22
class A:
    def __init__(self):
       
