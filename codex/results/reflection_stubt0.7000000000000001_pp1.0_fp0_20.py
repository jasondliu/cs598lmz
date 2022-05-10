fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
f(*gi)

class D(object):
    def __init__(self, v1, v2, v3):
        self.value1, self.value2, self.value3 = v1, v2, v3

class E(D):
    def __getattr__(self, attr):
        return None

    def __setattr__(self, attr, value):
        if attr == 'value1':
            self.__dict__['value1'] = value
        elif attr == 'value2':
            self.__dict__['value2'] = value
        elif attr == 'value3':
            self.__dict__['value3'] = value

class F(E):
    def __getattr__(self, attr):
        return None

    def __setattr__(self, attr, value):
        if attr == 'value1':
            self.__dict__['value1'] = value
        elif attr == 'value2':
            self.__dict__['value2']
