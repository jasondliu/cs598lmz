fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__module__ = 'module'
# fn.__defaults__ = 0 # no default
# fn.__dict__ = 0 # no dict
# fn.__closure__ = 0 # no closure
# fn.__annotations__ = 0 # no annotations

@pytest.mark.parametrize('key,value', [
    ('__code__', gi.gi_code),
    ('__name__', 'fn'),
    ('__module__', 'module'),
    ('__defaults__', None),
    ('__dict__', {}),
    ('__closure__', None),
    ('__annotations__', {}),
])
def test_attr(key, value):
    assert getattr(fn, key) is value
