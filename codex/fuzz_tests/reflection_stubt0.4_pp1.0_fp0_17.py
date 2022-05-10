fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_generator_send_exception
def gen():
    try:
        yield
    except Exception as e:
        yield e

def gen2():
    try:
        yield
    except:
        yield

def gen3():
    try:
        yield
    except Exception as e:
        yield

def gen4():
    try:
        yield
    except Exception as e:
        yield e
    except:
        yield

def gen5():
    try:
        yield
    except:
        yield
    except Exception as e:
        yield e

g = gen()
next(g)
g.send(Exception)

g = gen2()
next(g)
g.send(Exception)

g = gen3()
next(g)
g.send(Exception)

g = gen4()
next(g)
g.send(Exception)

g = gen5()
next(g)
g.send(Exception)

# test_generator_throw_exception
def gen():

