import types
types.ClassType.dispatch = dispatch
# ... these should be the only changes necessary to any class definition
#################################################################


def printBold(prtStr):
    print '\033[1m' + prtStr + '\033[0m'
    
def id():
    return 'cscirepo.mit.edu'

class ReposCatalogException(Exception):
    """
    An exception class for ReposCatalog errors.
    """
    def __init__(self, msg=None):
        if msg is None:
            msg = 'An unknown error has occured'
        self.msg = msg

    def __str__(self):
        return self.msg

class ReposCatalog(object):
    """
    A Catalog client class
    """
    def __init__(self, **kwargs):
        """
        Initialize the Catalog client class. If a dictionary
        of keyword arguments (kwargs) is passed, initialize
        from them. Otherwise, initialize from the environment.
        """
        if kwargs:
            # We were passed a dictionary of keywords and values

