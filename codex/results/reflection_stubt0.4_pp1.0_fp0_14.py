fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = types.CodeType(
    0, 0, 0, 0, b"", b"", (), (), (), "", b"", 0, b"")
fn.__code__.co_varnames = ("x", "y")
fn.__code__.co_argcount = 2
fn.__defaults__ = (1, 2)
fn.__kwdefaults__ = {"z": 3}
fn.__globals__ = {"spam": "ham"}
fn.__closure__ = (spam,)
fn.__annotations__ = {"x": 1, "y": 2}
fn.__doc__ = "Hello"
fn.__name__ = "foo"
fn.__qualname__ = "bar"
fn.__module__ = "baz"
fn.__dict__ = {"eggs": "spam"}
fn.__class__ = type
fn.__self__ = None
fn.__text_signature__ = "(x, y)"
fn.__get__ = lambda self, inst, cls: None
fn.__set__
