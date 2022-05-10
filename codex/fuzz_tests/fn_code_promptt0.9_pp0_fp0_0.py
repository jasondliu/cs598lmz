fn = lambda: None
# Test fn.__code__.co_argcount
ltests.append(["code",
               lambda: assert_equal(fn.__code__.co_argcount, 0),])
## fn.__code__.co_name
fn.__name__ = "xyz"
ltests.append(["code",
               lambda: assert_equal(fn.__code__.co_name, "xyz"),])
# Test fn.__code__.co_varnames
ltests.append(["code",
               lambda: assert_equal(fn.__code__.co_varnames, ()),])
# Test fn.__globals__ is set correctly
ltests.append(["code",
               lambda: assert_equal(fn.__globals__ is globals(), True),])

## fn.__code__.co_nlocals
fn = lambda x=7, y=0: y
ltests.append(["code",
               lambda: assert_equal(fn.__code__.co_nlocals, 2),])
ltests.append(["code",
               lambda: assert_equal
