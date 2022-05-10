import codecs
codecs.register_error('strict', codecs.ignore_errors)
import itertools
import operator
import re

_MAX_TITLE_LENGTH = 1024
_CHAR_SAFE = frozenset(string.letters+string.digits+"!()*._'")

_FILE_TAXA = 'taxa'
_FILE_TITLES = 'titles'


class SimpleFormatter(Formatter):
    """Format some text with a mapping, handling named and unnamed
    fields.  Named arguments override positions, and the "*" attribute
    overrides both, with a mapping slice."""

    def __init__(self, mapping=None):
        Formatter.__init__(self, mapping)

    def format_field(self, value, spec):
        if spec.startswith('.'):
            converted = self.format(value, spec[1:])
            return spec.startswith('.*') and converted or converted[0]
        else:
            return Formatter.format_field(self, value, spec)


class util(object):
    @staticmethod
    def debug
