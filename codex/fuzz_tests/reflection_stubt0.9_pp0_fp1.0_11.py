fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = i = type('')('', '', (), ())
gi.gi_frame = fn.__globals__['__builtins__'] = __import__('__main__')
sys.modules['__builtin__'] = __import__('__main__')
from itertools import *  # NOQA
import antigravity  # NOQA

if __name__ == '__main__':
    main()
