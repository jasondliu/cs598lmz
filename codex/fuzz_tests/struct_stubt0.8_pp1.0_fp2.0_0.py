from _struct import Struct
s = Struct.__new__(Struct)

class Struct:
    def __init__(self):
        print("In Struct init")
        self.__name = 'struct'
    def __call__(self):
        print("In Struct call")

s = Struct()
# s()
