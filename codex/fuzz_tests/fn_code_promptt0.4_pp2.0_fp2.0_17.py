fn = lambda: None
# Test fn.__code__
try:
    fn.__code__
except AttributeError:
    print("SKIP")
    raise SystemExit

# Test fn.__code__.co_name
try:
    fn.__code__.co_name
except AttributeError:
    print("SKIP")
    raise SystemExit

# Test fn.__code__.co_varnames
try:
    fn.__code__.co_varnames
except AttributeError:
    print("SKIP")
    raise SystemExit

# Test fn.__code__.co_argcount
try:
    fn.__code__.co_argcount
except AttributeError:
    print("SKIP")
    raise SystemExit

# Test fn.__code__.co_consts
try:
    fn.__code__.co_consts
except AttributeError:
    print("SKIP")
    raise SystemExit

# Test fn.__code__.co_code
try:
    fn.__code__.co_code
except AttributeError:
    print("SKIP
