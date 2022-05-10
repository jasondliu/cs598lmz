import types
# Test types.FunctionType

def test_function_type(space):
    def f():
        pass
    w_f = space.wrap(f)
    w_res = space.call_function(space.w_function, w_f)
    assert space.is_true(space.isinstance(w_res, space.w_function))
    assert space.eq_w(space.getattr(w_res, space.wrap('func_code')),
                      space.getattr(w_f, space.wrap('func_code')))
    assert space.eq_w(space.getattr(w_res, space.wrap('func_globals')),
                      space.getattr(w_f, space.wrap('func_globals')))
    assert space.eq_w(space.getattr(w_res, space.wrap('func_name')),
                      space.getattr(w_f, space.wrap('func_name')))
    assert space.eq_w(space.getattr(w_res, space.wrap('func_defaults')),
                      space.get
