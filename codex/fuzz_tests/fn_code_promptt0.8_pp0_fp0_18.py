fn = lambda: None
# Test fn.__code__ and fn.__qualname__
# fn.__defaults__ = ()
# fn.__globals__ = {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>}
# fn.__dict__ = {}
# fn.__closure__ = None
# fn.__code__ = <code object <module> at 0x107d09a50, file "/Users/honglongpham/Desktop/Python101/Functional/closure.py", line 1>
# fn.__name__ = '<module>'
# fn.__qualname__ = '<module>'
print(dir(closure))

# A closure is kind of like a function that is returned with the local environment snapshot.
def get_population_function(population):
    def get_local_population():
        return population
    return get_
