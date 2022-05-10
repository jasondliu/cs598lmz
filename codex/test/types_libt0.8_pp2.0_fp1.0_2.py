import types
types.FunctionType = lambda x: True
try:
    import json
except ImportError:
    import simplejson as json
import datetime

# Import the API
from . import API


class ExceptionWithAPI(Exception):
    """
    Base exception class with API message variable.
    """
    def __init__(self, *args, **kwargs):
        self.api_message = kwargs.pop('api_message', None)
        super(ExceptionWithAPI, self).__init__(*args, **kwargs)

class CallError(ExceptionWithAPI):
    """
    Exception that should be raised when the API call cannot be done due to errors in the request.
    """
    pass

class ServerError(ExceptionWithAPI):
    """
    Exception that should be raised when the API call returns an error.
    """
    pass

class ServerConnectionError(ExceptionWithAPI):
    """
    Exception that should be raised when there is an error connecting to the API server.
    """
    pass


