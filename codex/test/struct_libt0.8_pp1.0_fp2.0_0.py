import _struct

#--------------------------------------------------------------------

VERSION = "0.12"
URL = "http://www.voidspace.org.uk/python/modules.shtml#pyftpsync"

#--------------------------------------------------------------------
# ftp exceptions

class Error(Exception):
    """Base class for module exceptions."""
    pass

class FTPOSError(Error, OSError):
    """Exceptions raised when the underlying FTP class raises a ftplib.error_perm."""
    def __init__(self, source, err):
        self.args = (source, err)

    def __str__(self):
        return "FTPOSError: %s" % self.args[1]

class FTPSyncError(Error):
    """Exceptions raised when the two trees are incompatible."""
    def __init__(self, source, err):
        self.args = (source, err)

    def __str__(self):
        return "FTPSyncError: %s" % self.args[1]

#--------------------------------------------------------------------
# constants

IGNORE_CASE = 0
