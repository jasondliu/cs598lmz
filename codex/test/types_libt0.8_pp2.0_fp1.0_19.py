import types
types.FunctionType

class FileInfo(dict): 
    '''Store file metadata'''
    def __init__(self, filename=None): 
        self["name"] = filename
        self["type"] = "file"

class DirInfo(dict): 
    '''Store directory metadata'''
    def __init__(self, dirname=None): 
        self["name"] = dirname
        self["type"] = "directory"
        self["children"] = []

def walk(path): 
    print("walk", path)
    ''' Traverse a directory tree,
        yielding DirInfo and FileInfo objects '''
    try: 
        names = os.listdir(path) 
    except os.error: 
        return
    info = DirInfo(path)
    yield info
    for name in names: 
        fullname = os.path.join(path, name)
