import select
# Test select.select
def test_select_select():
    # check some obvious errors
    raises(TypeError, select.select, "foo", 3, 9)
    raises(TypeError, select.select, [], [], [], "bar")
    raises(TypeError, select.select, [], [], [], [])
    raises(TypeError, select.select, ["foo"], [], [])
    raises(TypeError, select.select, [3], [], [])
    # check some unexpected but still fairly obvious errors
    # (using garbage collectable objects)
    class Foo: pass
    raises(TypeError, select.select, [Foo()], [Foo()], [Foo()], 0)
    # check that it calls a file descriptor's fileno() method
    f = file('/dev/null')
    f.fileno = lambda: 42
    raises(select.error, select.select, [f], [], [], 0)
    f.fileno = lambda: -1
    raises(select.error, select.select, [f], [], [], 0)
    f
