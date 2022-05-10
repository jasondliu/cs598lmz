import bz2
bz2.BZ2File

class Enclosing(object):
    def __enter__(self):
        return 'test struct context'
    def __exit__(self, exc_type, exc_value, traceback):
        print(exc_type, exc_value, traceback)
        return True

def generate_squares(n):
    for i in range(n):
        yield i**2

from contextlib import contextmanager

@contextmanager
def nested(label):
    print('entering', label)
    try:
        yield
    except Exception:
        print('with exception', label)
    finally:
        print('exiting', label)

with nested('A'), nested('B'), nested('C'):
    print('inside with statement')

# with nested('C'):
#     print('inside A')
#     with nested('B'):
#         print('inside with')
#     print('inside B')
