import weakref

from . import errors
from . import strings
from . import types as t
from . import utils
from . import validators as v


class Field(object):
    """Base field class.

    All fields should inherit from this class.

    """
    #: Attribute name in the model.
    name = None
    #: Field type.
    type = None
    #: Argument to the field type.
    type_args = None
    #: Argument to the field type.
    type_kwargs = None

    #: `True` if the field is required.
    required = None

    #: Default value.
    default = None

    #: Validator or validators used to validate the value.
    validators = None

    #: Metadata.
    metadata = None

    #: `True` if the field can be serialized.
    serializable = None

    def __init__(self, *args, **kwargs):
        #: Field name.
        self.name = self.name or kwargs.pop('name', None)
        #: Field type
