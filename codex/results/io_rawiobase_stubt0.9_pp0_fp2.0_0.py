import io
class File(io.RawIOBase):
    def __init__(self,filename=None,mode=None):
        self.filename = filename
        self.mode = mode
        self.a = 1

    @classmethod
    def print_class_name(cls):
        print(cls.__name__)

    @staticmethod
    def print_static_method(x):
        print(x)

    @staticmethod
    def print_static_method():
        print(2312)

    def print_normal_method(self):
        pass



print(type(File()))
print(type(File.__init__))
print(type(File.print_class_name))
print(type(File.print_normal_method))
print(type(File.print_static_method))
