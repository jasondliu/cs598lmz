import types
types.SimpleNamespace
# class Simple_Namespace(BaseException):
#     '''Simple data holder.
#     A simple namespace object whose attributes can be set and accessed using
#     attribute notation (obj.name) and item notation (obj['name']).
#     '''
#     __slots__ = ()
#     def __init__(self, **kwargs):
#         for (k, v) in kwargs.items():
#             setattr(self, k, v)
#     def __repr__(self):
#         keys = list(self.__dict__.keys())
#         keys.sort()
#         items = ("{}={!r}".format(k, self.__dict__[k]) for k in keys)
#         return "{}({})".format(type(self).__name__, ", ".join(items))
#     def __eq__(self, other):
#         return vars(self) == vars(other)
#     def __contains__(self, name):
#         try:
#             getattr(self, name
