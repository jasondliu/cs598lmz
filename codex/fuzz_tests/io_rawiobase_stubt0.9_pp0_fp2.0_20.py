import io
class File(io.RawIOBase):
    def __init__(self, *args, **kwargs):
        # Dummy constructor - exists only to return a nice message
        raise NotImplementedError(
        """
        File does not support direct instantiation. Use `load` to load a file
        and `dump` to save a file.
        """
    )
    @staticmethod
    def load(path=None):
        # declare function to load file from path (defaults to cwd)
        f = File()
        # load file data
        with open(path, "r") as file_data:
            f.data = file_data.read()
        # return file object
        return f
    def dump(self, path=None, data=None):
        # declare function to write data to a file at path (defaults to cwd)
        # overwrite data if provided
        data = self.data if data is None else data
        # write data to file
        with open(path, "w") as file_data:
            file_data.write(data)
    @property
    def path(self):

