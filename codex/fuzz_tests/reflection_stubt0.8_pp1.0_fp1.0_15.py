fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__dict__ = {}
fn.__doc__ = ''
fn.__module__ = '__main__'
sys.modules[fn.__module__] = fn
try:
    from tests.test_utils import *
except ImportError:
    try:
        from test_utils import *
    except ImportError:
        print('Failed to import test_utils.py. Something is wrong with this project.')
        raise
try:
    from tests.test_interpreter import *
except ImportError:
    try:
        from test_interpreter import *
    except ImportError:
        print('Failed to import test_interpreter.py. Something is wrong with this project.')
        raise
try:
    from tests.test_errors import *
except ImportError:
    try:
        from test_errors import *
    except ImportError:
        print('Failed to import test_errors.py. Something is wrong with this project.')
        raise
try:
    from tests.test
