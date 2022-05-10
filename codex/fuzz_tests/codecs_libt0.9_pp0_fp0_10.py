import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

logger = logging.getLogger('buzhug')


def warn(message):
    print('\n    WARNING: %s\n' % message, file=sys.stderr)
    sys.stderr.flush()


class Database(object):
    """
    Abstract database based on the buzhug database, with some added
    functionality:

    - (yet) another syntax for column selection.
    - more robust database opening.
    - database can be read by multiple processes and is locked for writing
      and when creating/dropping tables.
    - table names contain no characters that can't be part of a file name.
    - tables can be *dropped* (in contrast to buzhug, where tables can only
      be overwritten).
    - database can be closed *without* writing ('rollback')
    - database can be read from and written to at the same time (although
      care must be taken to hold the database lock for short periods of time,
     
