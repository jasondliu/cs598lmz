fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

try:
    fn()
except TypeError:
    print('TypeError')

try:
    fn.__code__ = 1
except TypeError:
    print('TypeError')

try:
    fn.__code__ = 'a'
except TypeError:
    print('TypeError')

try:
    fn.__code__ = None
except TypeError:
    print('TypeError')

try:
    fn.__code__ = {'a': 1}
except TypeError:
    print('TypeError')

try:
    fn.__code__ = classmethod(lambda: None)
except TypeError:
    print('TypeError')

try:
    fn.__code__ = staticmethod(lambda: None)
except TypeError:
    print('TypeError')

try:
    fn.__code__ = property(lambda: None)
except TypeError:
    print('TypeError')

try:
    fn.__code__ = lambda: None
except TypeError:
    print('TypeError')

try:
