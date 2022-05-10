import weakref

from pymongo import MongoClient

from . import config

# default mongo database to use
_db = None

# default client to use
_client = None


def _get_client():
    """
    Get the current client, or create a new one if necessary.
    """
    global _client

    if _client is None:
        _client = MongoClient(config.MONGO_HOST, config.MONGO_PORT)

    return _client


def get_db(name=None):
    """
    Get the default database, or create a new one if necessary.
    """
    global _db

    if _db is None:
        _db = _get_client()[name or config.MONGO_DBNAME]

    return _db


#
# The following is a workaround for an issue with weakrefs and
# DBRefs.  Basically, if a DBRef is stored in a collection, then
# the collection gets deleted, the DBRef will not be able to
# resolve the collection.  This is because the DBRef is holding a
# weak reference
