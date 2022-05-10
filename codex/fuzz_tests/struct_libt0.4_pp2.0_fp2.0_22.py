import _struct

class _SimpleStruct(_struct.Struct):
    def __init__(self, format):
        _struct.Struct.__init__(self, format)
        self.size = self.size

class Struct(_SimpleStruct):
    def __init__(self, format):
        _SimpleStruct.__init__(self, format)
        self.size = self.size

class Struct_1(_SimpleStruct):
    def __init__(self, format):
        _SimpleStruct.__init__(self, format)
        self.size = self.size

class Struct_2(_SimpleStruct):
    def __init__(self, format):
        _SimpleStruct.__init__(self, format)
        self.size = self.size

class Struct_3(_SimpleStruct):
    def __init__(self, format):
        _SimpleStruct.__init__(self, format)
        self.size = self.size

class Struct_4(_SimpleStruct):
    def __init__(self, format):
        _SimpleStruct.__init__(self, format)
