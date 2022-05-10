fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
assert not explains(fn, 'no attribute')

# Avoid tripping over stack-unwinding code (e.g. when the VM is tp->frame_info)
enc = types.CodeType("dogfood", 0, 1, 400, 0, "", "", "", "", "", 0, "", (), ())
s = {'f': enc}
assert not explains(s, 'no value for key')

# Avoid further issues with boehm's GC.
fn = sqlite3_exec
fn.func_code = lambda: None

# .__dict__ is not included in __slots__
class C(object):
    __slots__ = ("__dict__",)
C().__dict__

import gc; gc.collect()

# Stringify the error
assert re.match(r"\<.*\>", explains(1, 'no value for key', min_str_len=0))
