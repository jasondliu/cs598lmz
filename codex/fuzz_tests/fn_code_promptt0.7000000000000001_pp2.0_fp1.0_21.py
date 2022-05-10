fn = lambda: None
# Test fn.__code__.co_argcount
try:
    fn.__code__.co_argcount
except:
    print("SKIP")
    raise SystemExit

print(fn.__code__.co_argcount)
print(fn.__code__.co_varnames)
print(fn.__code__.co_argcount)
print(fn.__code__.co_varnames)
