fn = lambda: None
gi = (i for i in ())
fn.__code__ = gen.gi_frame.f_code
gen.gi_frame.f_locals = {'.0': fn, 'i': 0}
gen.__name__ = 'generator_name'

# This is a generator, but it gets added in the *module* dict.
generator = gen(i for i in ())
generator.__name__ = 'generator'

# This is a function, but it gets added in the *module* dict.
fun = classmethod(lambda x: None)
fun.__name__ = 'fun_in_module'

# This is a nested class, but it gets added in the *module* dict.
class Cls:
    class Inner:
        pass
Cls.__name__ = 'Cls'
Cls.Inner.__name__ = 'Cls.Inner'

# This does not appear anywhere in the module.
class NotInModule:
    pass

# This is a function, but it gets added in the *submodule* dict.
submodule.subfun = lambda: None
submodule.subfun.__name__
