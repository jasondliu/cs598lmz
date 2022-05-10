import io
class File(io.RawIOBase):

    # use open to create an instance of File

    def readinto(self, b):
        """ read len(b) bytes into b """


class File:
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)
        self.__data = self.file_obj.read()

    def __getitem__(self, item):
        return self.__data[item]

    def __setitem__(self, key, value):
        self.__data[key] = value

    def __del__(self, key):
        del self.__data[key]

    def __str__(self):
        return str(self.__data)


file_name = 'my_file.txt'
file = File(file_name, 'w')
file.file_obj.write('Hello!')
file.file_obj.write(':)')

file.file_obj.close()

file = File(file_name, 'r')
print(file)

class File():

    def
