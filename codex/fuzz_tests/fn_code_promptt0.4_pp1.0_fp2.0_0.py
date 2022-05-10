fn = lambda: None
# Test fn.__code__.co_varnames
fn.__code__.co_varnames = "a"
fn.__code__.co_varnames = ("a", "b")
fn.__code__.co_varnames = ("a",)
fn.__code__.co_varnames = ()
# Test fn.__code__.co_argcount
fn.__code__.co_argcount = 3
# Test fn.__code__.co_flags
fn.__code__.co_flags = 0
fn.__code__.co_flags = 1
fn.__code__.co_flags = 2
fn.__code__.co_flags = 3
fn.__code__.co_flags = 4
fn.__code__.co_flags = 5
fn.__code__.co_flags = 6
fn.__code__.co_flags = 7
fn.__code__.co_flags = 8
fn.__code__.co_flags = 9
fn.__code__.co_flags = 10
fn.__code__.co_flags = 11

