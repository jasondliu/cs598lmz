import lzma
lzma.open

# Check for python 3
try:
    unicode
except NameError:
    # Python 3.x
    unicode = str


class ArNdb(object):
    """
    Utility class for working with ArangoDB collections.
    """
    def __init__(self, db, col_name="ndb"):
        self._db = db
        self._col = db.create_collection(col_name)
        if not self._col:
            self._col = db.collection(col_name)

    def dump(self, file_name):
        """
        Dump all objects, as documents, to a file. Returns the number of
        documents written.
        """
        counters = {}
        for t in self._db.type_map:
            counters[t] = 0
        with open(file_name, "w") as of:
            for d in self._col.all():
                of.write(json.dumps(d, default=lambda x: x.dict) + "\n")
                counters[d.get("_type")
