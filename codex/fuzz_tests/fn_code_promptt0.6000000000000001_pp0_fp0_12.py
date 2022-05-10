fn = lambda: None
# Test fn.__code__.co_varnames

def fn0(): pass
fn0.__code__.co_varnames
def fn1(a): pass
fn1.__code__.co_varnames
def fn2(a,b): pass
fn2.__code__.co_varnames
def fn3(a,b,c): pass
fn3.__code__.co_varnames
def fn4(a,b,c,d): pass
fn4.__code__.co_varnames
def fn5(a,b,c,d,e): pass
fn5.__code__.co_varnames

# Test fn.__code__.co_argcount

def fn0(): pass
fn0.__code__.co_argcount
def fn1(a): pass
fn1.__code__.co_argcount
def fn2(a,b): pass
fn2.__code__.co_argcount
def fn3(a,b,c): pass
fn3.__code__.co_argcount
def fn4(
