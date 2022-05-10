import types
types.ModuleType

def module_from_spec(spec, name, filename):
    mod = types.ModuleType(name)
    mod.__name__ = name
    mod.__file__ = filename
    exec(spec.loader.exec_module(mod), mod.__dict__)
    return mod

spec = importlib.util.spec_from_file_location("hello", "./hello.py")
hello = module_from_spec(spec, "hello", "./hello.py")

print(hello.hello("Tom"))
