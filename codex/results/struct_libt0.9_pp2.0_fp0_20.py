import _struct
from future.utils import iteritems


class DataStoreOptionsBuilder(object):
    """The ``DataStoreOptionsBuilder`` class builds a specific ``DataStoreOptions`` object.

    A ``DataStoreOptionsBuilder`` can be used to create a specific type of ``DataStoreOptions``.

    Creation::

       DataStoreOptionsBuilder builder = DataStoreOptionsBuilder()\
            .writeThrough(True)\
            .readThrough(True)\
            .statisticsEnabled(True)\
            .managementEnabled(True)\
            .hotspotPercentage(50)\
            .expiration(Expiration.afterWrite(60, TimeUnit.SECONDS))\
            .expiration(Expiration.afterAccess(30, TimeUnit.SECONDS))\
            .eviction(Eviction.maxEntries(10000))\
            .maxEntriesInCache(5000000)\
            .writeBehind(WriteMode.THROUGH, QueueSizing.FIFO(1000), 5, 50)\
            .persistenceFactory(new FilePersistenceFactory())\
            .resourceManagerFactory(new DefaultResourceManagerFactory())\
            .
