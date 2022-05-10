fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()
""")

    def test_code_getattr_1(self):
        self.assertCodeExecution("""
class MyInt(int):
    def __init__(self, value):
        self.value = value

    def __int__(self):
        return self.value

class MyFloat(float):
    def __init__(self, value):
        self.value = value

    def __float__(self):
        return self.value

def fn():
    pass

fn.__code__.co_consts = (1, 2, 3, 4, 5, 6, 7, 8)
fn.__code__.co_varnames = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
fn.__code__.co_numlocals = 8
fn.__code__.co_nlocals = 8

print(fn.__code__.co_consts)
print(fn.__code__.co_varnames)
print(fn.__code__.
