fn = lambda: None
# Test fn.__code__.co_varnames
fn.__code__.co_varnames = (1, 2, 3)
try:
    fn.__code__.co_varnames = (1, 2, 3, 4)
except TypeError:
    print("TypeError")
try:
    fn.__code__.co_varnames = (1, 2, 3, 4, 5)
except TypeError:
    print("TypeError")
try:
    fn.__code__.co_varnames = (1, 2, 3, 4, 5, 6)
except TypeError:
    print("TypeError")
try:
    fn.__code__.co_varnames = (1, 2, 3, 4, 5, 6, 7)
except TypeError:
    print("TypeError")
try:
    fn.__code__.co_varnames = (1, 2, 3, 4, 5, 6, 7, 8)
except TypeError:
    print("TypeError")
try:
    fn.__code__.co_varnames = (1
