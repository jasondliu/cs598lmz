from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

class Struct2(Struct):
    def __init__(self, format):
        pass

Struct2('i')
Struct2.size

class Struct3(Struct):
    def __init__(self, format):
        Struct.__init__(self, format)

Struct3('i')
Struct3.size

class Struct4(Struct):
    def __init__(self, format):
        pass
    def __new__(cls, format):
        return Struct.__new__(cls, format)

Struct4('i')
Struct4.size



# Issue #9805: test __getnewargs__ and __getnewargs_ex__
class C(object):
    def __getnewargs__(self):
        return ()

C().__reduce__()

class D(object):
    def __getnewargs_ex__(self):
        return (), {}

D().__reduce__()


# Issue #9815: test __getstate__ and __setstate__
