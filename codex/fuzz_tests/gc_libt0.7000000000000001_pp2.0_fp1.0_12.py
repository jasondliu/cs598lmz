import gc, weakref

class ModuleInfo:
    def __init__(self, module):
        self.module = module
        self.module.info = self
        self.name = module.__name__
        self.modpath = module.__file__
        self.doc = module.__doc__
        self.clsmembers = {}
        self.initmembers = []

        if self.name == '__main__':
            self.name = os.path.splitext(os.path.basename(self.modpath))[0]
            self.doc = "Script " + self.name

        for name in dir(self.module):
            object = getattr(self.module, name)
            if type(object) == types.ClassType:
                self.clsmembers[name] = object
            elif (type(object) == types.FunctionType) or \
                    (type(object) == types.BuiltinFunctionType):
                self.initmembers.append(name)

        self.initmembers.sort()
        self.clsmembers = self.clsmem
