import weakref

from . import utils


class _Base(object):
    """
    Base class for all storage backends.
    """
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def get_storage(self, name):
        """
        Returns a storage instance for the given name.
        """
        raise NotImplementedError

    def get_available_name(self, name):
        """
        Returns a filename that's free on the target storage system, and
        available for new content to be written to.
        """
        raise NotImplementedError

    def save(self, name, content):
        """
        Saves new content to the file specified by name. The content should be
        a proper File object or any python file-like object, ready to be read
        from the beginning.
        """
        raise NotImplementedError

    def delete(self, name):
        """
        Deletes the specified file from the storage system.
        """
        raise NotImplementedError


