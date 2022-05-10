fn = lambda: None
# Test fn.__code__.co_argcount
fn.__code__ = None
fn.__code__ = 30
fn.__code__ = 'abc'
fn.__code__ = []
fn.__code__ = {}
fn.__code__ = True
fn.__code__ = False
# Test fn.__code__.co_varnames
fn.__code__.co_varnames = None
fn.__code__.co_varnames = 5
fn.__code__.co_varnames = 'abc'
fn.__code__.co_varnames = []
fn.__code__.co_varnames = {}
fn.__code__.co_varnames = True
fn.__code__.co_varnames = False
# Test fn.__code__.co_flags
fn.__code__.co_flags = None
fn.__code__.co_flags = 5
fn.__code__.co_flags = 'abc'
fn.__code__.co_flags = []
fn.__code__.co_flags = {}
fn.__
