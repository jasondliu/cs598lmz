fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__doc__ = 'doc'
fn.__dict__ = {}
fn.__defaults__ = ()
fn.__closure__ = ()
fn.__globals__ = {}
fn.__annotations__ = {}
fn.__kwdefaults__ = None
fn.__module__ = '__main__'
fn.__qualname__ = 'fn'

# The following are not supported by PyPy
if not PYPY:
    fn.__text_signature__ = '(x, y)'
    fn.__self__ = None
    fn.__get__ = None
    fn.__set__ = None
    fn.__delete__ = None

# The following are not supported by Python 3.5
if sys.version_info >= (3, 6):
    fn.__state__ = None
    fn.__dict__ = {'a': 1}
    fn.__annotations__ = {'a': 1}
    fn.__kwdefaults__ = {'a': 1}
   
