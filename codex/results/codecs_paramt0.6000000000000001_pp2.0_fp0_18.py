import codecs
codecs.register_error('strict', codecs.ignore_errors)

_RE_UNI_NAME = re.compile("^([0-9A-F]{4,6})([^0-9A-F].*)?$", re.I)
_RE_DEC_NAME = re.compile("^([0-9]{1,5})([^0-9].*)?$")


def _get_codepoint(name):
    """
    Return the codepoint corresponding to the given name.
    """
    m = _RE_UNI_NAME.match(name)
    if m:
        return int(m.group(1), 16)
    m = _RE_DEC_NAME.match(name)
    if m:
        return int(m.group(1))
    raise ValueError("not a character name: %r" % name)


def _get_name(cp):
    """
    Return the name corresponding to the given codepoint.
    """
    return "U+%04X" % cp


def _normalize_names(
