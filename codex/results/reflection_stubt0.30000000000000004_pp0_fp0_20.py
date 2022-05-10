fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_code_setattr_invalid_type
def fn(): pass
fn.__code__ = 1
fn()

# test_code_setattr_invalid_type2
def fn(): pass
fn.__code__ = 'abc'
fn()

# test_code_setattr_invalid_type3
def fn(): pass
fn.__code__ = None
fn()

# test_code_setattr_invalid_type4
def fn(): pass
fn.__code__ = object()
fn()

# test_code_setattr_invalid_type5
def fn(): pass
fn.__code__ = [1, 2, 3]
fn()

# test_code_setattr_invalid_type6
def fn(): pass
fn.__code__ = (1, 2, 3)
fn()

# test_code_setattr_invalid_type7
def fn(): pass
fn.__code__ = {1, 2, 3}
fn()

# test_code_setattr_invalid_
