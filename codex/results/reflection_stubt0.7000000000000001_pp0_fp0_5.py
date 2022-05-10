fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()
"""
    for fn in [
        BytesIO,
        StringIO,
        open,
        lambda: open('/dev/null'),
        lambda: open('/dev/null', 'w'),
        lambda: open('/dev/null', 'wb'),
    ]:
        if fnname(fn) == 'BytesIO':
            assert fn().read(10) == b''
        else:
            assert fn().read(10) == ''
        run(fn, ('''
fn.__code__ = lambda x: x
'''))


def test_set_not_code():
    fn = lambda: None
    fn.__code__ = 1
    raises(TypeError, lambda: fn())
    fn.__code__ = 'hello'
    raises(TypeError, lambda: fn())
    fn.__code__ = 'hello'.encode('utf-8')
    raises(TypeError, lambda: fn())
    fn.__code__ = b'hello'
    raises(TypeError, lambda: fn())
