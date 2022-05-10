import mmap

#
#   Class:
#       <File>
#
#   This class is a wrapper for the file object.
#   It is used to read a file and return the content
#   as a string.
#
class File:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_object = None
        self.file_content = None

    def open(self):
        self.file_object = open(self.file_path, 'r')
        return self.file_object

    def close(self):
        self.file_object.close()

    def read(self):
        self.file_content = self.file_object.read()
        return self.file_content

    def get_content(self):
        return self.file_content

    def get_path(self):
        return self.file_path

#
#   Class:
#       <Directory>
#
#   This class is a wrapper for the os.walk()
#   function. It is used to return a
