import mmap
# Test mmap.mmap() to see if it supports offset
try:
    mmap.mmap(0, 1, "test", mmap.ACCESS_READ, offset=1)
except (ValueError, TypeError):
    HAVE_MMAP_EXTRA_ARGS = False
else:
    HAVE_MMAP_EXTRA_ARGS = True

def _get_fixed_width(context, text):
    """
    Helper function to calculate the fixed width of a piece of text
    """
    try:
        text_width = context.text_extents(text)[4]
    except (TypeError, AttributeError):
        # Either there is no context, or the text is not
        # unicode, so we just return the length of the text
        # and hope for the best.
        text_width = len(text)
    return text_width

def _ensure_type(value, type_or_tuple, _auto_type=None, _fallback_type=None):
    """
    Ensures that the input is of a given type.

    If the input is not a
