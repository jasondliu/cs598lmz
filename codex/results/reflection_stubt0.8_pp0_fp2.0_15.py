fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__code__.co_name == '<lambda>'

# __getstate__
class C():
    def __getstate__(self):
        return None

x = C()
pickle.dumps(x)
C.__getstate__ = lambda self: super().__getstate__()
x = C()
pickle.dumps(x)

# __init_subclass__
class C:
    def __init_subclass__(cls):
        staticmethod(type(None))

# __len__
class C(int):
    def __len__(self):
        return self.real

len(C())

# __length_hint__
class C:
    def __length_hint__(self):
        return 1
    def __getitem__(self, index):
        return 1
x = C()
sum(x)

# __mro_entries__
def f():
    pass
f.__globals__['__annotations__'] = None
f.__gl
