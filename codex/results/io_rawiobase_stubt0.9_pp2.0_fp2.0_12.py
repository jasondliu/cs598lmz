import io
class File(io.RawIOBase):
    """Fle object that works just like the python file but with an alternative __init__"""

    def __init__(self, *args, **kwargs):
        """Like the build in file init method but without the failfast flag added as raw files can't use it"""
        self.do_open(*args, **kwargs)

    def do_open(self, file: str = '', mode: str = 'r') -> None:
        """open the file given but only if it exists and is readable"""
        if mode != 'r':
            raise ValueError("File mode must be 'r' for file paths")
        if os.path.isfile(file):
            self.name = os.path.abspath(file)
            self.close()

        else:
            raise FileNotFoundError("File '{}' does not exist".format(file))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        return False
