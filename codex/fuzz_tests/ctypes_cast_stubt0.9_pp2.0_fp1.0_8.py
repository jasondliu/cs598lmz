import ctypes
ctypes.cast(ctypes.c_char_p(p.raw), ctypes.POINTER(MovableInt))


# ------------------- Enum --------------------------

class Enum(object):

    def __init__(self, names):
        self.__names = names
        for index, name in enumerate(names):
            setattr(self, name, index)
        self.__reverse = dict((index, name) for index, name in enumerate(names))

    def read(self, fo):
        i = read_int(fo)
        name = self.__reverse[i]
        self.value = name
        self.index = i
        return self

    def write(self, fo):
        return write_int(fo, self.index)

    def __str__(self):
        return self.value


# ------------------- Objects --------------------------

class Object(object):

    def __init__(self, **args):
        self.__dict__.update(args)


# ------------------- Struct ----------------------

class Struct(Object):

    @classmethod
    def read
