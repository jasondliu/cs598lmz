import ctypes

class S(ctypes.Structure):
    x = 2

if __name__ == '__main__':
    print dir(S)
    print S._fields_
    print S._fields_[0][0]
    print S._fields_[0][1]
    # print S.__dict__
    # print S._fields
    print S.x

    print issubclass(S, object)
