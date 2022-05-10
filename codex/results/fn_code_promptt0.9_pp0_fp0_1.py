fn = lambda: None
# Test fn.__code__
# fn.__code__ = code_obj
# fn.__name__ = code_obj.co_name
# fn.__globals__ = frame.f_globals
# fn.__defaults__ = code_obj.co_consts[0] if code_obj.co_flags & CO_VARARGS else None
# fn.__kwdefaults__ = code_obj.co_consts[1] if code_obj.co_flags & CO_VARKEYWORDS else None
# fn.__closure__ = (ccell for ccell in code_obj.co_freevars)
# fn.__annotations__ = code_obj.co_consts[2] if code_obj.co_flags & CO_VARARGS else {}
# fn.__call__ = lambda *args, **kwargs: fn.__code__(*args, **kwargs)
# del fn.__code__
# return fn


# def monkeypatch_instance(instance, new_attrs):
#     """
#     Monkeypatch an instance's attributes
#     """

