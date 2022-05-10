fn = lambda: None
# Test fn.__code__.co_consts
def test_co_consts():
    assert fn.__code__.co_consts == (None,)

# Test fn.__code__.co_varnames
def test_co_varnames():
    assert fn.__code__.co_varnames == ("")

# Test fn.__code__.co_argcount
fn = lambda x: None
def test_co_argcount():
    assert fn.__code__.co_argcount == 1

fn = lambda x,y=3: None
def test_co_argcount_with_defaults():
    assert fn.__code__.co_argcount == 2

fn = lambda x,*y: None
def test_co_argcount_varargs():
    assert fn.__code__.co_argcount == 2

fn = lambda x,      \
     **y: None
def test_co_argcount_kwargs():
    assert fn.__code__.co_argcount == 1

fn = lambda x,*y,z=5,**w
