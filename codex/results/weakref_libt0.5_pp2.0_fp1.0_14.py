import weakref

from . import base
from . import utils


class _Mock(base.Mock):
    """Mock a :class:`~pymongo.collection.Collection`."""

    def __init__(self, *args, **kwargs):
        """Initialize a :class:`~pymongo.collection.Collection` mock."""
        super().__init__(*args, **kwargs)
        self.database = DatabaseMock(self)
        self.name = kwargs.get('name', 'mock')
        self.full_name = '{}.{}'.format(self.database.name, self.name)
        self.write_concern = kwargs.get('write_concern', WriteConcern(0))

        self.client = weakref.ref(self.database.client)
        self.database = weakref.ref(self.database)
        self.write_concern = weakref.ref(self.write_concern)

    def __getitem__(self, item):
        """Get a collection by name."""

