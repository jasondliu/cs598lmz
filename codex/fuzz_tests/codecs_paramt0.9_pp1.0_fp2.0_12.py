import codecs
codecs.register_error("strict", codecs.ignore_errors)   # to surpress ascii codec error

# A note on codepages
# See: http://msdn.microsoft.com/en-us/goglobal/bb964654.aspx
#
# Algorithm for writing a module to read an EDF file:
#
# 1. Parse the header, first the header bytes, then follow the specified
#      order to read the header fields, making sure to respect the codepage
#      and return an edf-class object.
#
# 2. Parse the label fields


class VersionZeroReader(EdfReaderBase):

    eof = b'\xff' * 256

    def __init__(self, edf):
        super(VersionZeroReader, self).__init__(edf)
        self.signal_offset = self.edf.header_length
        self.signal_bytes = self.edf.signal_length

    @property
    def file_length(self):
        """The size of the original edf file, in bytes"""
        return len(
