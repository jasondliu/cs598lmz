import gc, weakref
import traceback
import warnings
import logging


def _is_valid_cld(cld):
    """
    See if a CursorListData is valid.
    """
    if cld is None:
        return False
    if not hasattr(cld, 'cursor'):
        return False
    if not hasattr(cld, 'data'):
        return False
    if cld.cursor is None:
        return False
    if cld.data is None:
        return False
    return True


def _has_cld(obj):
    """
    See if an object has CursorListData.
    """
    if not hasattr(obj, 'cursor_data'):
        return False
    cld = obj.cursor_data
    return _is_valid_cld(cld)


class CursorList(list):
    """
    A list that always has an associated Cursor in the CursorListData,
    and knows how to update the cursor.
    """
