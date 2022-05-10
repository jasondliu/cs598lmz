fn = lambda: None
# Test fn.__code__.co_code



# Test __file__
def test___file__():
    import sys
    import os
    assert __file__ == sys.argv[0]
    assert sys.argv[0] == os.path.abspath(sys.argv[0])

# Test __package__
def test___package__():
    import ast
    assert ast.__package__ == 'ast'

# Test __doc__
def test___doc__():
    assert len(__doc__) > 10

# Test __annotations__
def test___annoations__():
    def f(x: 42) -> 42:
        pass
    assert f.__annotations__ == {'x': 42, 'return': 42}

# Test __loader__
def test___loader__():
    import ast
    import sys
    assert ast.__loader__ == sys.modules[ast.__package__].__loader__
    assert sys.modules[ast.__package__].__loader__

# Test __spec__
def test___spec__():
    import ast
   
