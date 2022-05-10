from types import FunctionType
list(FunctionType(
    code, globs, name,
    defaults, closure))
'''

'''
# from functools import partial
# from types import FunctionType
# class partial(partial):
#     def _get_func(self):
#         return self.func
#     def __call__(self, *args, **kwargs):
#         return self.func(*(self.args + args), **dict(self.keywords, **kwargs))
#     def __reduce__(self):
#         return (FunctionType, (self.func, self.__globals__, self.__name__, self.__defaults__, self.__closure__))
#     def __reduce_ex__(self, protocol):
#         return (FunctionType, (self.func, self.__globals__, self.__name__, self.__defaults__, self.__closure__))
'''

'''
class partial(partial):
    def __reduce__(self):
        return (FunctionType, (self.func, self.__globals__,
