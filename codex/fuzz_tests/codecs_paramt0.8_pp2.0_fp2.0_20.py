import codecs
codecs.register_error('surrogate_or_strict', codecs.strict_errors)


class SQLiteOutput(OutputPlugin):
    """
    Output plugin for writing events to a SQLite database.
    """

    DEFAULT_DB = 'sqlite.db'
    DEFAULT_BATCH_SIZE = 100

    def __init__(self, event_stream, config=None, db=DEFAULT_DB, batch_size=DEFAULT_BATCH_SIZE):
        super(SQLiteOutput, self).__init__(event_stream, config)
        self.batch_size = batch_size
        self.db = db

    def get_db(self):
        if not hasattr(self, '_db'):
            self._db = sqlite3.connect(self.db, detect_types=sqlite3.PARSE_DECLTYPES)

        return self._db

    def init_table(self, event_type):
        db = self.get_db()

        # get the columns for this event type
        columns = self.get_event_columns(event_type
