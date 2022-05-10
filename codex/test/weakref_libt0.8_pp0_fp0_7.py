import weakref
import logging
import re

from .base import I, IF, IList, IS, R, S, C
from .environment import Environment, Slot, Object
from .components import (
    Name,
    Label,
    Element,
    Distance,
    Location,
    Orient,
    Shape,
    Layout,
    Appearance,
    Order,
    Associated,
    Classification,
    Instance,
    Domain,
    Icon,
    ClassProperties,
    Time,
    Scales,
    Query,
)
from .rules import RuleSet, Variable, bind
from . import utils
from .utils import fqn
from .errors import (
    ParserError,
    CompilerError,
    InterpretationError,
    ValidationError,
    UndefinedReference,
    UndefinedObject,
)
from . import version
from . import components
from . import primitives
from .primitives import isprimitive
