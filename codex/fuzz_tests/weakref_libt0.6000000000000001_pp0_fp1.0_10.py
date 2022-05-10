import weakref

class PyBind(object):
    '''
    This class is used to define the binding between a PyQt widget and a
    python object.
    '''
    
    def __init__(self, widget, obj, prop):
        '''
        The constructor is used to define the binding between a PyQt widget and a
        python object.
        
        :param widget: The PyQt widget that is bound.
        :type widget: QWidget
        :param obj: The python object that is bound.
        :type obj: object
        :param prop: The property name of the python object that is bound.
        :type prop: str
        '''
        self.__widget = widget
        self.__obj = weakref.ref(obj)
        self.__prop = prop
    
    def __get__(self, obj, objtype):
        '''
        This method is used to get the value of the property of the python object.
        
        :param obj: The python object that is bound.
        :type obj: object
        :param objtype: The type
