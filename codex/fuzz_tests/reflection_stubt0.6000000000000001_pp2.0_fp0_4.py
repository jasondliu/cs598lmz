fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

# empty tuple, no code
def fn(): pass
fn.__code__ = ()
fn()

# empty tuple, one element
def fn(): pass
fn.__code__ = ((),)
fn()

# empty tuple, two elements
def fn(): pass
fn.__code__ = ((), ())
fn()

# tuple with one element
def fn(): pass
fn.__code__ = ((0,),)
fn()

# tuple with one element, two elements
def fn(): pass
fn.__code__ = ((0,), ())
fn()

# tuple with one element, three elements
def fn(): pass
fn.__code__ = ((0,), (), ())
fn()

# tuple with two elements
def fn(): pass
fn.__code__ = ((0, 1),)
fn()

# tuple with two elements, two elements
def fn(): pass
fn.__code__ = ((0, 1), ())
fn()

# tuple with two elements, three elements
def fn(): pass
fn.__code__ = ((
