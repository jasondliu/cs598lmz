fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__doc__ = 'doc'
fn.__annotations__ = {'a': 1}
fn.__dict__ = {'d': 2}
fn.__kwdefaults__ = {'e': 3}
fn.__closure__ = (c,)
fn.__code__ = gi.gi_code
fn.__globals__ = {'g': 4}
fn.__qualname__ = 'fn'


class myclass:
    "doc"
    a = 1
    b = 2
    c = 3


class mydescr:

    def __get__(self, inst, class_):
        if inst:
            return self.data[inst]
        else:
            return self.data

    def __set__(self, inst, value):
        self.data[inst] = value

    def __delete__(self, inst):
        del self.data[inst]


class mydescrclass:

    def __get__(self, inst, class_):
       
