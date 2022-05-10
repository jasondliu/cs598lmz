import codecs
codecs.register_error('strict', codecs.ignore_errors)

#
# 
#
class File(object):
    """
    A class to represent a file.
    """
    def __init__(self, name, path, size, mtime):
        self.name = name
        self.path = path
        self.size = size
        self.mtime = mtime

#
# 
#
class Directory(object):
    """
    A class to represent a directory.
    """
    def __init__(self, name, path, mtime):
        self.name = name
        self.path = path
        self.mtime = mtime
        self.files = []
        self.dirs = []

#
# 
#
class FileSystem(object):
    """
    A class to represent a file system.
    """
    def __init__(self, path):
        self.path = path
        self.files = []
        self.dirs = []
        self.root = Directory(os.path.basename(path), path, os.
