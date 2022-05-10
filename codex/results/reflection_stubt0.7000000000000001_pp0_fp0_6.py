fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = "fn"
fn.__qualname__ = "fn"
fn.__annotations__ = {}
fn.__closure__ = None
fn.__globals__ = {}
fn.__kwdefaults__ = None
fn.__defaults__ = None
fn.__module__ = "test_module"
fn.__text_signature__ = "() -> None"
fn.__doc__ = None
fn.__dict__ = {}
fn.__qualname__ = "fn"
fn.__self__ = None

# Function with annotations
def fn_with_annotations(a: int, b: str, *args, c: float, d: complex, **kwargs) -> list:
    pass

# Function with annotations and defaults
def fn_with_annotations_defaults(a: int = 0, b: str = "", *args, c: float = 1.0, d: complex = 1j, **kwargs) -> list:
    pass

# Function with annotations and kwonly defaults
def fn_with
