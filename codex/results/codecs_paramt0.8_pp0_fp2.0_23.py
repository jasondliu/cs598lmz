import codecs
codecs.register_error("strict", codecs.strict_errors)

class Stream:
    """
    A wrapper around a Python StringIO object that facilitates limited
    lookahead and lookbehind.
    """

    def __init__(self, file, name=None):
        """
        Initialize the stream.
        """
        if name:
            self.name = name
        else:
            try:
                self.name = file.name
            except AttributeError:
                self.name = "stream"

        if type(file) == unicode:
            file = file.encode("utf-8")

        self.string = codecs.getreader("utf-8")(file)
        self.reset()

    def reset(self):
        self.string.seek(0)
        self.cache = Queue(maxsize=3)
        self.eof = False
        self.line = 1
        self.column = 0

    def __iter__(self):
        """
        Iterate through the stream, yielding each character.
        """
        for char in self.string.read
