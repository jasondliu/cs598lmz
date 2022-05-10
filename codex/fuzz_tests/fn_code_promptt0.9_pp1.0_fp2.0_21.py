fn = lambda: None
# Test fn.__code__ is an attribute
fn.__code__

# Is fn a function?
inspect.isfunction(fn)

fn.__code__.co_varnames
fn.__code__.co_argcount
fn.__code__.co_flags
fn.__code__.co_code
rm
rm.__code__
rm.__code__.co_flags
fn.__code__.co_code == rm.__code__.co_code

# Inspecting annotations
from functools import wraps

def add_hello(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print("Hello")
        return fn(*args, **kwargs)
    return wrapper

@add_hello
def greet(name: str) -> str:
    return f"Hi, {name}"

fn.__code__.co_code
rm.__code__.co_code
greet.__code__.co_code
greet.__annotations__

"""
6.5 Function introspection...
"""

# dir()
