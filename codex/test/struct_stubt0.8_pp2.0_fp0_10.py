from _struct import Struct
s = Struct.__new__(Struct)
print(s)

class MyStruct(Struct):
    def __init__(self, name, value):
        super().__init__(name, value)
        self.name = name
        self.value = value
        self.__obj = self
        self.__type = type(self)

    def _keys(self):
        return ['name', 'value']

    def __getattr__(self, name):
        return getattr(self, name)

    def __setattr__(self, name, value):
        setattr(self, name, value)

    def _mutable(self):
        return True

    def _asdict(self):
        attrs = self._keys()
        return {key: getattr(self, key) for key in attrs}

    def __repr__(self):
        return 'MyStruct({}, {})'.format(self.name, self.value)

myStruct = MyStruct('hello', 'world')
print(myStruct.name)
print(myStruct)
print(myStruct._asdict())
