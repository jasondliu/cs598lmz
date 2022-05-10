import codecs
codecs.register_error('strict', codecs.ignore_errors)

# -----------------------------------------------------------------------------
# 
# -----------------------------------------------------------------------------

class FileSystem(object):
    """
    FileSystem is a class that provides a common interface for accessing
    files and directories.
    """
    def __init__(self, path):
        self.path = path
    
    def __str__(self):
        return self.path
    
    def __repr__(self):
        return '<%s: %s>' % (self.__class__.__name__, self.path)
    
    def __eq__(self, other):
        return self.path == other.path
    
    def __ne__(self, other):
        return self.path != other.path
    
    def __lt__(self, other):
        return self.path < other.path
    
    def __le__(self, other):
        return self.path <= other.path
    
    def __gt__(self, other):
        return self.path > other.path
    
    def __ge__(
