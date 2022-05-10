import gc, weakref

class Object(object):
    '''
    A base class for objects.
    
    :param _name: The name of the object.
    :type _name: str
    '''
    
    def __init__(self, _name=None):
        '''
        Initializes the object.
        '''
        self._name = _name
        self._parent = None
        self._children = []
        self._callbacks = []
        self._type = self.__class__.__name__
        self._type_id = id(self)
        self._type_ref = weakref.ref(self)
        self._cached_data = {}
        self._saved_data = {}
        self._saved_data_stack = []
        self._objects = {}
        self._objects_list = []
        self._objects_dirty = False
        self._objects_dict = {}
        self._objects_dict_dirty = False
        self._root = None
        self._is_root = False
        self._is_root_dirty = False
       
