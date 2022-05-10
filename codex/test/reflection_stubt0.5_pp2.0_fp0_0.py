fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code

import sys
sys.modules.pop('sys')

sys.modules['sys'] = fn
sys.modules['sys'].__code__ = gi.gi_code

import sys
