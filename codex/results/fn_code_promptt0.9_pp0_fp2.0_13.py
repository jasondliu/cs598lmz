fn = lambda: None
# Test fn.__code__.__sizeof__()
fn.__code__.__sizeof__()

# Test type(fn).__code__.__sizeof__()
type(fn).__code__.__sizeof__()

# Test type(fn).__code__.__sizeof__(fn)
type(fn).__code__.__sizeof__(fn)


# Test builtin.__staticmethod__.__sizeof__()
fn = staticmethod(lambda: None)
# Test fn.__func__.__code__.__sizeof__()
fn.__func__.__code__.__sizeof__()

# Test type(fn).__func__.__code__.__sizeof__()
type(fn).__func__.__code__.__sizeof__()

# Test type(fn).__func__.__code__.__sizeof__(fn)
type(fn).__func__.__code__.__sizeof__(fn)


# Test builtin.__classmethod__.__sizeof__()
fn = classmethod(lambda: None)

