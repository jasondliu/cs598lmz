import codecs
codecs.register_error('strict', codecs.ignore_errors)

from wand.image import Image
import os

class FileStorage(object):
    """FileStorage is an abstraction layer over the local filesystem.

    This is an abstract class that provides an interface for the
    class implementing it to define these methods.

    Parameters
    ----------
    None

    Returns
    -------
    Returns an instance of the class implementing the abstract class.

    """
    def __init__(self):
        pass

    def __activate__(self, context):
        """
        Called when the filter is initialized.

        Parameters
        ----------
        context : org.python.core.PyObject
            Contains the initializing servlet context.

        Returns
        -------
        None

        """
        self.velocityContext = context
        self.log = context["log"]
        self.file_path = context["file_path"]
        self.request = context["request"]
        self.response = context["response"]
        self.sessionState = context["sessionState"]
        self.config = context["systemConfig"]

        if self.
