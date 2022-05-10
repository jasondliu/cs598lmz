import io
class File(io.RawIOBase):
    
    def __init__(self, name):
        self.name = name
        self.buffer = None
        self.eof = True

file = File('file_name.txt')
print(f'File name: {file.name}')

class File:
    
    def __init__(self, name):
        self.name = name
        self.buffer = None
        self.eof = True

A = File('File.txt')
print(f'{A.name}')

class File:
    
    def __init__(self, name):
        self.name = name
        self.buffer = None
        self.eof = True

A = File('File.txt')
print(f'{A.name}')

B = A
print(f'{B.name}')

A.name = 'File_2.txt'
print(f'{B.name}')

class File:
    
    def __init__(self, name):
        self.name = name
        self.buffer = None

