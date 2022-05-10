gi = (i for i in ())
# Test gi.gi_code.co_flags to make sure the generator is not optimized out
# at the module level.
assert 0x40000 & gi.gi_code.co_flags

# Test a function generator.

def f():
    yield 1
    yield 2
    yield 3

assert f.__code__.co_flags & 0x40000

tf = f()
assert tf.gi_code.co_flags & 0x40000
try:
    gl = tf.gi_frame.f_locals
except ValueError as e:
    assert str(e) == 'generator already executing'
else:
    assert False, "expected ValueError"
assert tf.__name__ == 'f'
assert tf.__qualname__ == 'f'
assert tf.gi_code.co_name == 'f'
assert tf.gi_code.co_filename == __file__
assert tf.gi_frame.f_code.co_name == 'f'
assert tf.gi_frame.f_code.co_filename == __file__
try:
    tf.gi_frame.f
