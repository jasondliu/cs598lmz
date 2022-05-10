import weakref, copy
try:
    import pysvn
except ImportError:
    import os
    #print "SVN not installed, I will use a fake repository instead"
    pysvn = os.path
    import shutil
    import glob
    import tempfile
    ######################################################################
    ## fake pysvn
    ######################################################################
    class pysvn_Client(object):
        def __init__(self, *args):
            self.last_checkout_dir = ""
        def checkout(self, url, path, *args, **kwargs):
            self.last_checkout_dir = path
    class pysvn_WcInfo(object):
        def __init__(self, *args):
            self.repos_root_url = args[0]
        def commit(self, *args, **kwargs):
            pass
    class pysvn_ClientException(Exception):
        def __init__(self, *args):
            pass
