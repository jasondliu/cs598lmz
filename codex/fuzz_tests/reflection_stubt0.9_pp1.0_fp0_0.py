fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.__code__
globals()['t'] = fn()

# /Users/a1/Documents/git/study/python/pyevent/imp.py:178: in load_module
#     module = FIELD(FIELDS)
# w_code = Constant(0x7265766f63616c6c)
setattr(gi, '__code__', 'revocall')
getattr(fn, 't', 'revocall')(1)
#
"""


"""
In [1]: sys.path.append('/Users/a1/Documents/git/study/python/pyevent')                             

In [2]: import imp                                                                                  

In [3]: w_code = imp.new_module('poc')                                                              

In [4]: gi = (i for i in ())                                                                        

In [5]: gi.gi_code = w_code                                                                         

In [6]: sys.modules['poc'] = gi                                                                     

In [9]:
