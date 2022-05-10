import types
types.ClassType = type

from .OptParse import option_group
from .import pubsub

class ResourceNotFoundError(pubsub.PuPyBaseException):
    pass
class DuplicateError(pubsub.PuPyBaseException):
    pass

class NoSuchResourceError(Exception):
    pass
class ResourceTimeoutError(Exception):
    pass

class ResourceCreator(object):
    
    def __init__(self, resource_type, name, options=''):
        self.resource_type = resource_type
        self.name = name
        self.options = options

    def add_create_options(self, options, defaults):
        raise NotImplementedError()

    def check_opts(self, opts):
        raise NotImplementedError()

    def create(self, opts, prefix):
        if self.options:
            opts = self.options
            opts = opts.replace('$prefix', prefix)
