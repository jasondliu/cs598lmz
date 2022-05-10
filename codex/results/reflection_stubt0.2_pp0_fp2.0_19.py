fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__doc__ = 'doc'
fn.__dict__ = {'key': 'value'}
fn.__defaults__ = (1, 2, 3)
fn.__closure__ = (c1,)
fn.__globals__ = {'a': 1, 'b': 2}
fn.__annotations__ = {'a': 1, 'b': 2}
fn.__kwdefaults__ = {'a': 1, 'b': 2}

# test pickling of builtin functions
for proto in range(pickle.HIGHEST_PROTOCOL + 1):
    for name in dir(builtins):
        fn = getattr(builtins, name)
        if not isinstance(fn, types.BuiltinFunctionType):
            continue
        for module in (None, 'builtins'):
            if module is None:
                try:
                    fn2 = pickle.loads(pickle.dumps(fn, proto))
                except pickle.PicklingError:
                    continue

