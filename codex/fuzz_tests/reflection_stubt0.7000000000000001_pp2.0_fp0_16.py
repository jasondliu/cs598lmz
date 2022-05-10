fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()
""")

add_pytest('test_code_object_unpack_unsupported_kwargs', """
code_object_unpack_unsupported_kwargs = ('__kwdefaults__',)

def code_object_unpack(co):
    assert all(hasattr(co, k) for k in code_object_unpack_supported_kwargs)
    assert any(hasattr(co, k) for k in code_object_unpack_unsupported_kwargs)
    raise ValueError
""")

add_pytest('test_code_object_unpack_unsupported_kwargs_complicated', """
code_object_unpack_unsupported_kwargs = ('__kwdefaults__',)
code_object_unpack_supported_kwargs = ('co_argcount',)

def code_object_unpack(co):
    assert any(hasattr(co, k) for k in code_object_unpack_unsupported_kwargs)
    assert all(hasattr(co, k) for k in code_object_
