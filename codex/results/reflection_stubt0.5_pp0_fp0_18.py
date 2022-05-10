fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = "fn"

with pytest.raises(TypeError):
    fn()

# An exception is raised if the object is a function, but has no code object
fn = lambda: None

with pytest.raises(TypeError):
    fn.__code__ = None
    fn()

# An exception is raised if the object is a function, but has no code object
fn = lambda: None

with pytest.raises(TypeError):
    fn.__code__ = ""
    fn()

# An exception is raised if the object is a function, but has a code object
# with a different type
fn = lambda: None

with pytest.raises(TypeError):
    fn.__code__ = 1
    fn()
