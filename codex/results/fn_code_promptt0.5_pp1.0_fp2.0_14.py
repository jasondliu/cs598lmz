fn = lambda: None
# Test fn.__code__.co_varnames
fn.__code__.co_varnames = (1, 2, 3)
try:
    fn.__code__.co_varnames = (1, 2, 3, 4, 5, 6, 7, 8)
except ValueError:
    print("ValueError")
try:
    fn.__code__.co_varnames = (1, 2, 3, 4, 5, 6, 7, 8, 9)
except ValueError:
    print("ValueError")
try:
    fn.__code__.co_varnames = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
except ValueError:
    print("ValueError")
try:
    fn.__code__.co_varnames = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
except ValueError:
    print("ValueError")
try:
    fn.__code__.co_varnames = (1, 2, 3, 4, 5, 6, 7, 8
