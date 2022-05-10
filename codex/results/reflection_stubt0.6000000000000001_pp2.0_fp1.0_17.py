fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
try:
    fn()
except TypeError as e:
    print(e)

print('\n\n')

fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
try:
    fn()
except TypeError as e:
    print(e)

print('\n\n')

class MyException(Exception):
    pass

def fn():
    raise MyException

fn.__code__ = None
try:
    fn()
except MyException as e:
    print(e)

print('\n\n')

class MyException(Exception):
    pass

def fn():
    raise MyException

fn.__code__ = None
try:
    fn()
except MyException as e:
    print(e)
