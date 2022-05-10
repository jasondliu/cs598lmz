import codecs
# Test codecs.register_error('codec_test', codec_test) import
codecs.register_error('codec_test', codec_test)

class WrapperBase(object):
    """Baseclass for content wrappers.

    This class provides all the properties that can be used to get or set
    properties of a content object. They are not implemented in the baseclass,
    but raise a NotImplementedError instead."""

    def __repr__(self):
        return '<%s object "%s">' % (self.__class__.__name__, self.name)

    def __str__(self):
        return '<%s object "%s">' % (self.__class__.__name__, self.name)

    @property
    def content(self):
        """
        Property: the content of the content object.

        It returns a binary string.

        :Exceptions:
           - `PathError`: Raised when the content object does not exist.
           - `WriteError`: Raised when the content object could not be created.
        """
        raise NotImplemented
