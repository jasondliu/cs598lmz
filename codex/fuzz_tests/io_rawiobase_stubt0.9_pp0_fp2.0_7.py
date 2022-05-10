import io
class File(io.RawIOBase):
    def __init__(self, filename, *args, **kwargs):
        r"""
        Args:
            filename (str): Path to file.
        """
        super().__init__(*args, **kwargs)
        self.__f = open(filename, "rb")
        self.__name = filename  # for __repr__
        self.__out = None

    def readable(self):
        r"""Install `open()` hook that reads from disk when called."""
        return True

    def __repr__(self):
        try:
            return f"<torch.serialization.io.File[{self.__name}]>"
        except AttributeError:
            return f"<torch.serialization.io.File[closed]>"

    def __reduce__(self):
        r"""Compatibility hook for pickle."""
        if self.closed:
            return super().__reduce__()
        else:
            return type(self), (self.__name,)

    @property
    def input_stream(self):
        r
