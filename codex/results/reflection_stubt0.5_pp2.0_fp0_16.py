fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

# test_generator_finalization

def f():
    try:
        yield
    finally:
        print("finally")

g = f()
next(g)
del g
import gc
gc.collect()

# test_generator_finalization_2

def f():
    try:
        yield
    finally:
        print("finally")

g = f()
next(g)
del g
import gc
gc.collect()

# test_generator_finalization_3

def f():
    try:
        yield
    finally:
        print("finally")

g = f()
next(g)
del g
import gc
gc.collect()

# test_generator_finalization_4

def f():
    try:
        yield
    finally:
        print("finally")

g = f()
next(g)
del g
import gc
gc.collect()

# test_generator_finalization_5

def f
