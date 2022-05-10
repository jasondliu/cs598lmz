fn = lambda: None
# Test fn.__code__ or fn.__closure__,
# which was added in 2.6 or 3.0, oh well.
fn.__code__ = fn.__code__ or 0

#
# Time and Date 
#

def _constant_time_compare(val1, val2):
    """Returns True if the two strings are equal, False otherwise.

    The time taken is independent of the number of characters that match.  Do
    not use this function for anything else than comparison of hashes of known
    length, or when the content is secret (because it will leak length info).
    """
    if len(val1) != len(val2):
        return False
    result = 0
    for x, y in izip(val1, val2):
        result |= ord(x) ^ ord(y)
    return result == 0

#
# Versions and Version Ranges
#
#   Used by the dependency checker to test if certain packages
#   (eg, MarkupSafe) are present in the right version
#

class _Version(object):
    # THE MISSING DOC
