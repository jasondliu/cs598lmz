fn = lambda: None
# Test fn.__code__; this doesn't work on Python 2.7 or lower.
try:
    print(fn.__code__)
except AttributeError:
    print('That attr not available.')
 
# Test if fn.__code__.co_constants exists and is not equal to None.
if hasattr(fn.__code__, 'co_constants') and fn.__code__.co_constants != None:
    print(fn.__code__.co_constants)
s = ['a', 'b', 'c']
t = ('d', 'e', 'f')
u = (1, 2, 3)

is_sequence_like(s)
is_sequence_like(t)
is_sequence_like(u)
def get_animal_noise(animal_name, volume='normal'):
    if volume == 'quiet':
        suffix = '...'
    else:
        suffix = '!'
    d = {
        'dog': 'woof' + suffix,
        'pig': 'oink' + suffix,
        'duck': '
