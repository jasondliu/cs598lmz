fn = lambda: None
# Test fn.__code__.co_argcount
setattr(fn, "__code__", type("", (), {}))
fn()
# Test fn.__code__.co_kwonlyargcount
setattr(fn, "__code__", type("", (), {"co_argcount": 1}))
fn()
# Test fn.__code__.co_varnames
setattr(fn, "__code__", type("", (), {"co_argcount": 1, "co_kwonlyargcount": 1}))
fn()
# Test fn.__code__.co_flags
setattr(
    fn,
    "__code__",
    type(
        "",
        (),
        {
            "co_argcount": 1,
            "co_kwonlyargcount": 1,
            "co_varnames": (1, 2),
            "co_name": "fn",
        },
    ),
)
fn()


def test_valid_code_object():
    from cytoolz import compose

    f = lambda: None

    def g(a, b=None):
       
