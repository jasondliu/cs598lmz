import io
class File(io.RawIOBase):
    
    def __init__(self):
        pass
    
    def read(self):
        pass
    
    def write(self):
        pass
        
class FileReader(File):
    
    def __init__(self):
        pass
    
    def read(self):
        print('Read file')
    
    
class FileWriter(File):
    
    def __init__(self):
        pass
    
    def write(self):
        print('Write file')
    
    
class FileCreator:
    
    def __init__(self):
        pass
    
    def get_file(self, type_file):
        if type_file == 'read':
            return FileReader()
        elif type_file == 'write':
            return FileWriter()
        else:
            raise ValueError('No such file')
        
        
creator = FileCreator()
file = creator.get_file('read')
file.read()

file = creator.get_file('write')
file.write()

file = creator.get_
