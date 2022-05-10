fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# this is a generator-iterator
gi2 = (i for i in ())
# make it a code object:
# > In [19]: gi2.__code__
# > Out[19]: <code object <genexpr> at 0x7f96f312cf60, file "<ipython-input-18-0dafb3e7a25f>", line 1>
# >
# > In [20]: gi2.__code__.co_consts
# > Out[20]: (<code object <genexpr> at 0x7f96f312cf60, file "<ipython-input-18-0dafb3e7a25f>", line 1>,)
# >
# > In [21]: gi2.__code__.co_consts[0]
# > Out[21]: <code object <genexpr> at 0x7f96f312cf60, file "<ipython-input-18-0dafb3e7a25f>", line 1>
# >
# > In [22]: gi2.
