import codecs
codecs.register(make_identity)


class UnicodeString(str):
    """
    A string class that can contain Unicode strings.

    >>> UnicodeString('Parameter Value = \u9a0e\u68a8')
    UnicodeString('Parameter Value = 驮梨')

    This class doesn't do any transcoding, so the original encoding must be
    known in order to do any transcoding.

    Note this class doesn't support the ``StringIO`` interface.
    """

    @classmethod
    def from_string(cls, string):
        """
        Convert a Python bytes string to a :py:class:`UnicodeString` object.

        >>> UnicodeString.from_string(b'Parameter Value = \xe9\xa9\xae\xe6\xa2\xa8')
        UnicodeString('Parameter Value = 驮梨')
        """
        return cls(string)

    @classmethod
    def from_bytes(cls, bytestring, encoding='utf_8'):
        """
        Convert a Python bytestring to a :py
