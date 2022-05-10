fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

load_extension = fn = lambda: None
fn.__code__ = gi

get_cwd = fn = lambda: None
fn.__code__ = gi

listdir = fn = lambda d: []
fn.__code__ = gi

getcwd = fn = lambda: b''
fn.__code__ = gi

getenv = fn = lambda v: None
fn.__code__ = gi

setenv = fn = lambda v, s: None
fn.__code__ = gi

get_compiler_info = fn = lambda: b''
fn.__code__ = gi

getenvb = getenv
setenvb = setenv

sys.modules['_frozen_importlib'] = sys.modules['_frozen_importlib_external'] = None
sys.modules['_frozen_importlib_external'].__file__ = __file__
sys.modules['_frozen_importlib.abc'] = sys.modules['_frozen_importlib_external.abc'] = None

sys.byteorder
