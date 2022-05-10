fn = lambda: None
gi = (i for i in ())
fn.__code__ = [0, gi]

# Unlink the stored generator
fn.__code__[1] = None

# Hack fn back into the f_code of the builtin method for dir()
dir.__func__.__code__ = fn.__code__


import antigravity
logging.info('voila!')
