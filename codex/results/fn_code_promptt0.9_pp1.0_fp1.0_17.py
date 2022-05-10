fn = lambda: None
# Test fn.__code__.co_varnames
fn.__code__.co_varnames()
# Test pdb._getval()
import pdb
pdb._getval('test')
