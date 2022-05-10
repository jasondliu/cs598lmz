import codecs
codecs.register_error('strict', codecs.ignore_errors)


logger = logging.getLogger(__name__)
debug, verbose, info, warn, error = logger.debug, logger.debug, logger.info, logger.warn, logger.error

_XOR_KEY_STRING = 'JKTOLWKOTNRVDN'
_XOR_KEY = [ord(c) for c in _XOR_KEY_STRING]
_NoEscape = re.compile(r'[\x00-\x1f\x7f]')


def _xor_string(s):
    return ''.join(chr(ord(a) ^ ord(b)) for (a, b) in zip([char for char in s], itertools.cycle(_XOR_KEY)))


def _clean_s(s):
    return _NoEscape.sub('', s)


def _make_atom(c, s):
    assert(c == ':')
    return (':' + _clean_s(s), c)


def _make_string(c
