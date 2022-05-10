import weakref

class TType():
    """Base type object.

    Attributes:
        name: The module name of the type.
        type: The type as defined in the module.
        stub: The stub for this type.
    """
    name = ""
    type = None
    stub = None

    def __init__(self, name=None, type=None, stub=None):
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if stub is not None:
            self.stub = stub
        if (not self.name or not self.type or not self.stub):
            raise ValueError("name, type and stub cannot be None")

    def __repr__(self):
        return "<TType %s>" % (self.name)

class TService():
    """Base service object.

    Attributes:
        name: The module name of the service.
        service: The service as defined in the module.
        stub: The stub for this service.
    """
    name = ""
   
