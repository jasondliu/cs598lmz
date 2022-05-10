fn = lambda: None
# Test fn.__code__.co_freevars
globals().update(fn.__globals__)
# Test str.__getitem__
assert "0"[0] == "0"
assert True[0] == False[0] is True # bool inherits int. PyPy.

# Test PyCode_GetNumFree
assert fn.__code__.co_freevars == ()
def f():
    a = 1
    b = 2
    exec("c = 100")
assert f.__code__.co_freevars == ("b", "a")
assert f.__closure__[0].cell_contents == 2
assert f.__closure__[1].cell_contents == 1
# Test nb_index
assert (1)[0] == 1+(0) # int inherits object. PyPy.
assert (1,2)[0] == 1
assert [[1],2,3][0] == [1]
assert [1,2,3][-1] == 3
assert (1,2,3)[-1] == 3
assert (1,2,3)[0:-
