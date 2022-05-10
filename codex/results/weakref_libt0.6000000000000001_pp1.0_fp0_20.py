import weakref
import logging


logger = logging.getLogger(__name__)


class Base(object):
    """
    Base class.
    
    Every class that wants to be visible to the user must inherit from Base.
    """
    def __init__(self, *args, **kwargs):
        """
        Constructor.
        
        :param args: list of arguments to be passed to the constructor of the
            class inheriting from Base.
        :param kwargs: list of keyword arguments to be passed to the constructor
            of the class inheriting from Base.
        """
        self._instances = set()
        self._id = None
        self._name = None
        self._parent = None
        self._children = []
        self._user_data = {}
        self._callbacks = []
        self._visible = True
        self._disabled = False
        self._enabled = True
        self._on_click = None
        self._on_click_args = []
        self._on_click_kwargs = {}
        self._on_change = None
       
