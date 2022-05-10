fn = lambda: None
# Test fn.__code__.co_firstlineno
# Test fn.__code__.co_flags
# Test fn.__code__.co_names
# Test fn.__code__.co_varnames

# Check all values are documented
for const in dir(test_fn.__code__):
    if not isinstance(getattr(test_fn.__code__, const), int):
        continue
    if const.startswith('CO_') and const.upper() != const:
        # Skip values that aren't in ALL_CO
        if ALL_CO is None or const not in ALL_CO:
            continue
        if (const + '\n') not in open(__file__).read():
            print('WARNING: Missing documentation for %s = %d' %
                  (const, getattr(test_fn.__code__, const)))
