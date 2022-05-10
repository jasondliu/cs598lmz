import types
types.ModuleType.__getattr__ = lambda s, m: getattr(s, m, None)

# Add dummy module "site" as Python does
try:
    from importlib import machinery
    import imp
    import sysconfig
    _s = machinery.SourceFileLoader("site", sysconfig.get_path("purelib") + "/site.py").load_module()
except:
    _s = imp.new_module("site")
sys.modules["site"] = _s

# Add fake module "__main__" as Python does
_m = imp.new_module("__main__")
sys.modules["__main__"] = _m
_m.__dict__["__file__"] = sys.argv[0]

# Set sys.path
sys.path = [os.path.dirname(sys.executable)] + sys.path

# Add fake module "pkg_resources" as Python does
try:
    import _frozen_importlib
    _p = _frozen_importlib.FrozenImporter("pkg_resources").load_module("pkg_resources")
