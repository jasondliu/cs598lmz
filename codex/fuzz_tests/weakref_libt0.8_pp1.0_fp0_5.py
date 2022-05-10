import weakref

from pymongo.collection import Collection

from mongolog.log import BaseLog
from mongolog.utils import convert_to_document, convert_to_timestamp, dbref_wref, ObjectId, DocumentObjectId


class Log(BaseLog):
    """
    Log object that contains a list of documents.

    @ivar collection: the collection containing the log
    @type collection: pymongo.collection.Collection
    @ivar documents: list of the log's documents
    @type documents: list
    @ivar _id: the log's primary key
    @type _id: Basestring or int
    """

    def __init__(self, collection, name=None, documents=[], _id=None):
        """
        Create a log instance, optionally specifying its documents.

        @param name: the name of the log
        @type name: str
        @param documents: list of this log's documents
        @type documents: list
        @param _id: unique ID
        @type _id: str or int
        """
        if not isinstance(collection
