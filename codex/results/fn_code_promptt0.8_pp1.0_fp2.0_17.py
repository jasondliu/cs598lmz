fn = lambda: None
# Test fn.__code__
# fn.__code__
# Test fn.__closure__
# fn.__closure__
# @property
# def test(self):
#     return self.x
# 
# test.__get__
# 
# http://docs.python.org/2/reference/datamodel.html#customization
# 
# http://stackoverflow.com/questions/35681198/change-default-arguments-of-a-python-method-at-run-time
# 
# def get_bindings(member):
#     if hasattr(member, '__closure__'):
#         return dict([(var.__name__, val) for var, val in zip(member.__code__.co_freevars, member.__closure__)])
#     else:
#         return {}
#
# def set_default(member, **kwargs):
#     dst_bindings = get_bindings(member)
#     # TODO: Handle function defaults
#     dst_bindings.update(kwargs)
#     member.__
