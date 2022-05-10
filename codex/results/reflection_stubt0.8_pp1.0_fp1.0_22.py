fn = lambda: None
gi = (i for i in ())
fn.__code__ = \
        gi.gi_code = \
        (None,) * 7
gv = _sitebuiltins.global_variables()
fn.__globals__ = \
        gi.gi_frame.f_globals = \
        gv
fn.__name__ = \
        gi.gi_name = \
        gv['__main__']
del gi, gv

def enable_import_in_main(only_import_builtins=False):
    sys.meta_path.append(FinderSaver(sys.meta_path))
    sys.modules['__main__'] = sys.modules['__main__'].__class__('__main__')
    sys.modules['__main__'].__dict__.update(fn.__globals__)
    if not only_import_builtins:
        sys.modules['__main__'].__dict__.update(fn.__globals__)
        sys.modules['__main__'].__dict__['__builtins__'] = sys.modules['__builtins__
