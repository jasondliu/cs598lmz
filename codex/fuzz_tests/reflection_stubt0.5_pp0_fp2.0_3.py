fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__call__()

# from http://bugs.python.org/issue5295
def f():
    try:
        yield
    except Exception:
        pass

# from http://bugs.python.org/issue5295
def f():
    try:
        yield
    except ValueError:
        pass
    except Exception:
        pass

# from http://bugs.python.org/issue5295
def f():
    try:
        yield
    except:
        pass

# from http://bugs.python.org/issue5295
def f():
    try:
        yield
    except:
        pass
    finally:
        pass

# from http://bugs.python.org/issue5295
def f():
    try:
        yield
    finally:
        pass

# from http://bugs.python.org/issue5295
def f():
    try:
        yield
    except:
        pass
    else:
        pass

# from http://bugs.python.org/issue5295
def f():
