import types
types.MethodType = types.MethodType


class ClassA(object):
    def __init__(self):
        self.a = 'a'
        self.m_a = types.MethodType(A, self)

class ClassB(object):
    def __init__(self):
        self.b = 'b'
        self.m_b = types.MethodType(B, self)

class ClassC(ClassA, ClassB):
    def __init__(self, **kwargs):
        self.name = kwargs.pop('name', '')
        print('ClassC init.')
        super(ClassC, self).__init__(**kwargs)
        print('ClassC init successfully')
        pprint(self.__dict__)

    def C(self):
        print(self.name, self.a, self.b)

def A(self):
    print(self.name, self.a)

def B(self):
    print(self.name, self.b)


c = ClassC(name = 'code')
