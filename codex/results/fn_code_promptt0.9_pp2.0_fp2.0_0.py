fn = lambda: None
# Test fn.__code__.co_varnames
test_fn.__code__.co_varnames == None
test_fn.__code__.co_argcount == 0

test_fn.__code__.co_argcount == 0

# EAFP way
def test_fn_eafp():
    try:
        return next(x for x in range(5) if x == 10)
    except StopIteration:
        return "Iteration went over and done"

test_fn_eafp()


# EAFP way - Homework: iter() accepts iterator or an iterable
def eafp_function(iterable):
    try:
        iterator = iter(iterable)
        return next(iterator)
    except StopIteration:
        return print("Hi")


eafp_function(iter([1])) == 1

# EAFP way - Homework: iter() accepts iterator or an iterable
def eafp_function(iterable):
    try:
        iterator = iter(iterable)
        return next(iterator)
    except StopIteration:
       
