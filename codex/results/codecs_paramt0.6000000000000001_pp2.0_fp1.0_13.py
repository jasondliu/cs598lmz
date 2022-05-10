import codecs
codecs.register_error('strict', codecs.ignore_errors)

class InvalidFileTypeException(Exception):
    pass

class InvalidFilePathException(Exception):
    pass

class FileNotFoundException(Exception):
    pass

class FileReader(object):
    def __init__(self):
        pass

    def get_text(self, file_path):
        """
        Reads the file located at file_path and returns its contents as a string.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundException('File not found at path: ' + file_path)
        file_type, encoding = mimetypes.guess_type(file_path)
        if file_type is None:
            raise InvalidFileTypeException('Invalid file type for file at path: ' + file_path)
        if file_type.startswith('text'):
            with open(file_path, 'r') as file:
                return file.read()
        else:
            raise InvalidFileTypeException('Invalid file type for file at path: ' + file_path
