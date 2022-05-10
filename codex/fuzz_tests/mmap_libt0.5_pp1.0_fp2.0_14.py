import mmap
import json

from . import utils

logger = logging.getLogger(__name__)

class Cache(object):
    """
    A class for caching the results of a function call.
    """
    def __init__(self, cache_dir, cache_name, serialization_format='json'):
        """
        Parameters
        ----------
        cache_dir : str
            The directory where the cache file will be stored.
        cache_name : str
            The name of the cache file.
        serialization_format : str
            The format used to serialize the data. The options are:
            'json' (default) and 'pickle'.
        """
        self.cache_dir = cache_dir
        self.cache_name = cache_name
        self.serialization_format = serialization_format
        self.cache_file = os.path.join(self.cache_dir, self.cache_name)
        self.data = {}

    def set(self, key, value):
        """
        Set the value for a key.

        Parameters

