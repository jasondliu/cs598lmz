import codecs
codecs.register_error('strict', codecs.ignore_errors)

class FileWriter(object):
    def __init__(self, file_name, mode='w'):
        self.file_name = file_name
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = codecs.open(self.file_name, self.mode, 'utf-8', 'strict')
        return self.file

    def __exit__(self, type, value, traceback):
        self.file.close()

def get_file_list(path, extension='.txt'):
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(extension):
                file_list.append(os.path.join(root, file))
    return file_list

def get_file_name(path):
    return os.path.basename(path)

def get_file_extension(path):
    return os.path.
