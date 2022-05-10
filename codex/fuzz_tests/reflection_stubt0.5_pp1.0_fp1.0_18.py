fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_bad_type_code
fn = lambda: None
fn.__code__ = {}
fn()

# test_bad_type_defaults
fn = lambda: None
fn.__defaults__ = {}
fn()

# test_bad_type_kwdefaults
fn = lambda: None
fn.__kwdefaults__ = {}
fn()

# test_bad_type_annotations
fn = lambda: None
fn.__annotations__ = {}
fn()

# test_bad_type_closure
fn = lambda: None
fn.__closure__ = {}
fn()

# test_bad_type_globals
fn = lambda: None
fn.__globals__ = {}
fn()

# test_bad_type_name
fn = lambda: None
fn.__name__ = {}
fn()

# test_bad_type_doc
fn = lambda: None
fn.__doc__ = {}
fn()

# test_bad_type_module
fn = lambda: None
fn.__module__
