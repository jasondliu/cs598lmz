import codecs
codecs.register_error('strict', codecs.StrictError)

from itertools import chain
from collections import deque

from .table import Table, Row


class CSVError(Exception):
    pass


class CSVToTableAdapter:
    """ Turn a lazily-read CSV into a Table. """
    def __init__(self, handle):
        self.handle = handle
        # We buffer this because the csv API lets you seek back to the beginning
        # of the file, which we need to do for the headers
        self._rows = deque()
        self._col_names = None
        self._col_definition = None

    def _csv_rows(self):
        # Do we need to guess the dialect?
        dialect = csv.get_dialect(csv.Sniffer().sniff(self.handle.read(4096)))
        self.handle.seek(0)
        reader = csv.reader(self.handle, dialect=dialect)
        # Now construct row objects
        return (Row(row, self.column_names(), self.column_types())
               
