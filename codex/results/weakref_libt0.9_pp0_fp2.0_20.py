import weakref

from .constants import PROPERTY_CREATED_AT, PERMISSION_READ, PERMISSION_GROUP_READ, PERMISSION_WRITE
from .database import get_db
from .exceptions import ForbiddenException, RecordNotFoundException, HasConnectionException, NoConnectionException
from .query_filters import FilterType
from .utils import Singleton


def _get_obj(ref):
    """Return a ref to an instance or None"""
    if ref:
        return ref()
    return None


def _get_default_owner():
    """Get owner information for a new object"""
    return {"user_id": 1, "group_id": 1}


def _get_default_permission():
    return {
        "user_id": PERMISSION_WRITE,
        "group_id": PERMISSION_GROUP_READ,
        "other_id": PERMISSION_READ,
    }


def _set_argument_defaults(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        """
