fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
try:
    fn()
except TypeError:
    print('TypeError')

# __code__ is a writable descriptor
def fn(): pass
fn.__code__ = 1
try:
    fn()
except TypeError:
    print('TypeError')

# __code__ is a writable descriptor
def fn(): pass
fn.__code__ = None
try:
    fn()
except TypeError:
    print('TypeError')

# __code__ is a writable descriptor
def fn(): pass
try:
    fn.__code__ = 1
except TypeError:
    print('TypeError')

# __code__ is a writable descriptor
def fn(): pass
try:
    fn.__code__ = None
except TypeError:
    print('TypeError')

# __code__ is a writable descriptor
class C:
    def __init__(self):
        self.__code__ = 1

try:
    C()
except TypeError:
    print('TypeError')

# __code__ is a writable descriptor
class C:
