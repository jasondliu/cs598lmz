import codecs
# Test codecs.register_error('fallback', encodefallback)

# Python 3 has strict checking of the calling conventions for
# codecs.register_error() but PyPy doesn't.
if sys.version_info >= (3,):
    import _codecs
    if type(_codecs.register_error) != type(register_error):
        del _codecs
else:
    _codecs = codecs

# Regexps for language tag.
LANG_PAT = re.compile(
    r"""
    ^
    ([ix](?:\-[a-z0-9]+)*)   # language identifiers (open-ended alphanums)
    (?:\-([a-z0-9]+))?      # possible country (single alphanum)
    (?:\-([a-z0-9]+))?      # possible script (single alphanum)
    (?:\-([a-z0-9]+))?      # possible variant (single alphanums)
    $
    """, re.VERBOSE)

# Shortcuts to support routines:

