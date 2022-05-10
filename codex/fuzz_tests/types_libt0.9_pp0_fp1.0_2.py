import types
types_new = types.ModuleType("types")
types_new.__dict__.update(types.__dict__)
types = types_new
class ModuleType:
    def __init__(self, name, wxModule):
        self.name = name
        self.wxModule = wxModule
    def __import__(self, name, g, l, fromlist):
        if name != self.wxModule:
            f = open("%(i)s/%(name)s.py" % {"i" : mydir}, "rt")
            module = types.ModuleType(name)
            module.__file__ = "%(i)s/%(name)s.py" % {"i" : mydir, "name" : name}
            code = compile(f.read(), "%(i)s/%(name)s.py" % {"i" : mydir, "name" : name}, "exec")
            exec code in module.__dict__
            g[name] = module
            return module
        if not hasattr(g, self.name):
            g[
