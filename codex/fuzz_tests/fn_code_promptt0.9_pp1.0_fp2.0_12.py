fn = lambda: None
# Test fn.__code__ of a generator
fn.__code__ = fn.__code__.__class__(fn.__code__.co_argcount,
                                    fn.__code__.co_nlocals,
                                    fn.__code__.co_stacksize,
                                    fn.__code__.co_flags,
                                    fn.__code__.co_code,
                                    fn.__code__.co_consts,
                                    fn.__code__.co_names,
                                    fn.__code__.co_varnames,
                                    fn.__code__.co_filename,
                                    fn.__code__.co_name,
                                    fn.__code__.co_firstlineno,
                                    fn.__code__.co_lnotab,
                                    fn.__code__.co_freevars,
                                    fn.__code__.co_cellvars)
fn.__closure__ = (None,)
# ensure that the name is not in the local namespace
locals()[fn.__name__] = None
self.module.
