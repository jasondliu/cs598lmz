import codecs
codecs.register_error("ignore", codecs.lookup_error("ignore"))

class UnixFriendlyWriter(object):
    """
    A class that inherits from csv.writer, but changes the default line
    terminator from \\r\\n to \\n. This is useful for writing out csv
    files on Windows which will be read in elsewhere.
    """

    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
        # Redirect output to a queue
        self.queue = cStringIO.StringIO()
        self.writer = csv.writer(self.queue, dialect=dialect, **kwds)
        self.stream = f
        self.encoder = codecs.getincrementalencoder(encoding)()

    def writerow(self, row):
        self.writer.writerow([s.encode("utf-8") for s in row])
        # Fetch UTF-8 output from the queue ...
        data = self.queue.getvalue()
        data = data.decode("utf-8")
        # ... and
