fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__qualname__ = 'fn'
fn.__module__ = 'test'
fn.__defaults__ = ()
fn.__kwdefaults__ = None
fn.__annotations__ = {}
fn.__dict__ = {}
fn.__closure__ = None
fn.__globals__ = {}
fn.__doc__ = None
fn.__text_signature__ = None

# Test function with annotations
def fn_annotations(a: int, b: str = 'b', *args: int, c: int = 1, d: int = 2, **kwargs: int) -> int:
    pass

def fn_annotations_defaults(a: int, b: str = 'b', *args: int, c: int = 1, d: int = 2, **kwargs: int) -> int:
    return a + b + c + d

fn_annotations.__defaults__ = (1, 2)
fn_annotations.__kwdefaults__ = {'c':
