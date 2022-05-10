import weakref
import warnings
from . import Packer, Unpacker
from .compat import with_metaclass
from .constants import TYPE_REGISTRY
from .types import Integer, String, Float
from .utils import ensure_string, structural_equal


_logger = logging.getLogger(__name__)


def default_object_unpacker_hook(obj, attributes):
    """Default object unpacker hook.

    Supports structures of the following types:

    1. ``namedtuple``
    2. ``enum.Enum``
    3. MutableMapping
    4. MutableSequence

    If none of the above are satisfied, returns a plain empty ``dict``.

    :param obj: Object to construct.
    :param attributes: Attributes to initialize the object's attributes with.
    """
    if isinstance(obj, (tuple, list)):
        # Try to instantiate an enum with the provided attributes (enum's are
        # always iterable).
        try:
            return obj(attributes)
        except Exception:
            pass

        # Try to instant
