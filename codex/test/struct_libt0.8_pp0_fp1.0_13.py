import _struct
import _socket
import _asyncore

def start_new_thread(function, args, kwargs = {}):
    return thread.start_new_thread(function, args, kwargs)
    
class error (Exception):
    def __init__(self, err):
        self.err = err
        self.args = (err, )
        
    def __str__(self):
        return 'winsock error: %s' % self.err
    
class timeout (Exception):
    def __init__(self):
        self.args = ('timed out', )
    
    def __str__(self):
        return self.args[0]
    
class getdefaulttimeout (object):
    def __init__(self):
        self._timeout = None
    
    def __get__(self, obj, objtype = None):
        return self._timeout
    
    def __set__(self, obj, value):
        self._timeout = value
    
    def __delete__(self, obj):
        self._timeout = None

get
