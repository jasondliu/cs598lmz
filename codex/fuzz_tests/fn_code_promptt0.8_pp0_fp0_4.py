fn = lambda: None
# Test fn.__code__.co_varnames
fn.__code__ = lambda: None
# Test fn.__code__.co_freevars
fn.__code__ = lambda: None
# Test fn.__code__.co_cellvars
fn.__code__ = lambda: None


@meta_custom_test(test_list=[
    {'type': 'builtin', 'name': 'object'},
])
def test_type_object(**kwargs):
    # Test type.__name__
    @meta_custom_test(test_list=[
        {'type': 'builtin', 'name': 'object'},
    ])
    def fn(**kwargs2):
        return fn.__name__

    # Test type.__doc__
    fn.__doc__ = 'doc'
    # Test type.__module__
    fn.__module__ = 'module'


@meta_custom_test(test_list=[
    {'type': 'builtin', 'name': 'object'},
])
class C:
    # Test type.__mro__

