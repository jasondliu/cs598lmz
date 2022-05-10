import weakref

from ..utils import (
    AttrDict,
    fqn,
    FQN,
    log,
    get_call_info,
)
from ..types import (
    types,
    Enum,
    Type,
)
from ..exceptions import (
    TypeCheckError,
    DefinitionError,
    CyclicDependencyError,
    CircularDependencyError,
)


class Variable(object):

    """
    A class describing a type checker variable.

    :param name: The name of the variable.
    :param type: The type of the variable.

    .. attribute:: name

        The name of the variable.

    .. attribute:: type

        The type of the variable.

    """

    def __init__(self, name, type):
        self.name = name
        self.type = type
