fn = lambda: None
# Test fn.__code__
try:
    fn.__code__
except AttributeError:
    pass
else:
    raise TestFailed("__code__ exists on function objects")

# Test fn.func_code
try:
    fn.func_code
except AttributeError:
    pass
else:
    raise TestFailed("func_code exists on function objects")

# Test class.__code__
try:
    class_ = fn.__class__
except AttributeError:
    pass
else:
    try:
        class_.__code__
    except AttributeError:
        pass
    else:
        raise TestFailed("__code__ exists on class objects")

# Test class.func_code
try:
    class_ = fn.__class__
except AttributeError:
    pass
else:
    try:
        class_.func_code
    except AttributeError:
        pass
    else:
        raise TestFailed("func_code exists on class objects")

# Test instance.__code__
try:
    class_ = fn.__class__
except
