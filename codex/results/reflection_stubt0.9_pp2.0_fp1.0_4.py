fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.__code__
del gi
# Note: there is no version of this test for non-co_firstlineno code objects
# (i.e. generators, etc.).
# Issue 9485.
# This next test is designed to trigger a segmentation fault on an unpatched
# PyPy3 3.2.   It used to trigger a memory error on the reference interpreter
# prior to the patch for issue 9949.
self = b'!' * 6000  # (1)
def hook(cmd, label, filename):
    self, empty = '', ''
    self += '    ' + empty.join(cmd) + '\n'
    return self
sys.__interactivehook__ = hook
_ = input('')
del sys.__interactivehook__, hook


def f(code, *args, **kwargs):
    import dis
    dis.dis(code)
    co = compile(code, '', 'exec')
    exec(co, *args, **kwargs)
    exec(code, *args, **kwargs)
f('import sys\n_ =
