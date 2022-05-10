fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = "foo"
fn.__module__ = "bar"

class C:
    def __init__(self):
        self.__code__ = gi.gi_code
        self.__name__ = "foo"
        self.__module__ = "bar"

print(fn.__code__.co_name)
print(C().__code__.co_name)
