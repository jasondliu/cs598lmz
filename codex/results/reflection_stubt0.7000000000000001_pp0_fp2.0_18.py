fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

# Regression test for:
# https://sourceforge.net/tracker/?func=detail&aid=2934984&group_id=5470&atid=105470
# Note that this test does not hang, it segfaults.
gi_code = type(gi.gi_code)
fn = lambda: None
fn.__code__ = gi_code()
fn()

# Regression test for:
# https://sourceforge.net/tracker/?func=detail&aid=2935182&group_id=5470&atid=105470
# Note that this test does not hang, it segfaults.
gi_code = type(gi.gi_code)
fn = lambda: None
fn.__code__ = gi_code.__new__(gi_code)
fn()
