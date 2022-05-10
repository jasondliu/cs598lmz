fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()
 
# The following should raise a TypeError, but it doesn't
#fn = lambda: None
#fn.__code__ = (i for i in ())
#fn()

# The following should raise a TypeError, but it doesn't
#fn = lambda: None
#fn.__code__ = (i for i in ())
#fn.__code__.co_code = (i for i in ())
#fn()

# The following should raise a TypeError, but it doesn't
#fn = lambda: None
#fn.__code__ = (i for i in ())
#fn.__code__.co_code = (i for i in ())
#fn.__code__.co_code.co_filename = (i for i in ())
#fn()

# The following should raise a TypeError, but it doesn't
#fn = lambda: None
#fn.__code__ = (i for i in ())
#fn.__code__.co_code = (i for i in ())
#fn.__code__.co_code.co_filename = (
