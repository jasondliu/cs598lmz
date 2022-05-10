fn = lambda: None
# Test fn.__code__.co_varnames
fn.__code__.co_varnames = ()
# Test fn.__code__.co_filename
fn.__code__.co_filename = '__main__.py'
# Test fn.__code__.co_name
fn.__code__.co_name = 'fn'
# Test fn.__call__
fn.__call__()
# Test fn.__dict__.items
fn.__dict__.items()
# Test fn.__getattribute__
fn.__getattribute__('__name__')
# Test fn.__format__
fn.__format__('')
# Test fn.__doc__
fn.__doc__
# Test fn.__repr__
fn.__repr__()
# Test fn.__str__
fn.__str__()
# Test fn.__lt__
fn.__lt__(True)
# Test fn.__le__
fn.__le__(True)
# Test fn.__eq__
fn.__eq__(True)
# Test fn.__ne__
fn
