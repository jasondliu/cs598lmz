import weakref

from . import get_logger
from . import util

logger = get_logger(__name__)


class Client(object):
    """
    A client class to manage the connection to the server.

    .. code-block:: python

        client = Client('localhost')
        client.connect()

        # Create a new table if one doesn't exist.
        if 'example' not in client.list_tables():
            client.create_table('example')

        # Insert some data.
        client.write_points([
            {
                'measurement': 'cpu',
                'tags': {
                    'host': 'server01',
                    'region': 'us-west'
                },
                'time': '2009-11-10T23:00:00Z',
                'fields': {
                    'value': 0.64
                }
            }
        ])

        # Query the database.
        results = client.query('select value from cpu;')

        # Iterate over the results.
        for point in results.get_points():
            print('{
