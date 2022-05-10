import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------

class File(object):
    """
    Represent a file.
    """

    def __init__(self, path, name, size, mtime, ctime, mode, uid, gid, type):
        """
        Constructor.

        @param path Path of the file.
        @param name Name of the file.
        @param size Size of the file.
        @param mtime Modification time of the file.
        @param ctime Creation time of the file.
        @param mode Mode of the file.
        @param uid User ID of the file.
        @param gid Group ID of the file.
        @param type Type of the file.
        """

        self.path = path
        self.name = name
        self.size = size
        self.mtime = mtime
        self.ctime = ctime
        self.mode = mode
        self.uid = uid
        self.gid = gid
        self.type = type

#-------------------------------------------------------------------------------

class Directory(
