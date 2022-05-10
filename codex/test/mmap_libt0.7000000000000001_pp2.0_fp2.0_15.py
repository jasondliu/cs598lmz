import mmap

class IOUtils:
        
    def __init__(self):
        pass
    
    def load_file(self, filePath):
        f = open(filePath, 'r')
        data = f.read()
        f.close()
        return data
    
    def load_big_file(self, filePath):
        with open(filePath, 'r') as f:
            mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
            data = mm.read()
        return data
    
    def write_file(self, filePath, data):
        f = open(filePath, 'w')
        f.write(data)
        f.close()
        return True
    
    def create_directory(self, directoryPath):
        if not os.path.exists(directoryPath):
            os.makedirs(directoryPath)
        return True
    
    def get_file_names(self, directoryPath):
        fileNames = []
