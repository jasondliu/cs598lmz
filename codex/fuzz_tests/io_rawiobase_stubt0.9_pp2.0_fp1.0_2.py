import io
class File(io.RawIOBase):
    """ A file-like object that saves python code when written to."""
    def __init__(self, output):
        self.file = open(output, 'wb')
        if self.file:
            print("Output file", output, "opened.")
    def write(self, b):
        self.file.write(b.splitlines(True))
        self.file.write(b'\n')
    def close(self):
        self.file.close()
        print("Output file closed.")

class NotImplementedException(Exception):
    pass

class Preprocessor():
    def __init__(self, path = '', file = sys.stdout, debug = False, silent = False):
        self.debug = debug
        self.silent = silent
        self.config = self.load_config(path)
        self.output_file = self.make_file(file)
    def load_config(self, path):
        no_config_file = 'No config file found!'
        default_config = '{}/config/default.json'.format(
