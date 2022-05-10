fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = types.CodeType(
    0, 0, 0, 0, b'', b'', (), (), (), '', b'', 0, b'')
fn.__globals__ = gi.gi_frame.f_globals
gi.gi_frame.f_globals['__name__'] = __name__
sys.modules[__name__] = fn

# Import the actual module.
from . import _multiprocessing

# Now fix up the module name.
fn.__name__ = _multiprocessing.__name__
fn.__package__ = _multiprocessing.__package__
fn.__file__ = _multiprocessing.__file__
fn.__doc__ = _multiprocessing.__doc__
fn.__path__ = _multiprocessing.__path__
fn.__loader__ = _multiprocessing.__loader__
fn.__spec__ = _multiprocessing.__spec__
fn.__dict__.update(_multiprocessing
