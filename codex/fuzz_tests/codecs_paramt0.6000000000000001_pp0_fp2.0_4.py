import codecs
codecs.register_error("strict", codecs.ignore_errors)

import re
import os
import sys

from . import common
from . import globs
from . import utils
from . import config

class BadMapping(Exception):
    pass

class BadMappingFile(Exception):
    pass

class Mapping(object):
    """
    A mapping that translates one string to another.
    """
    def __init__(self, pattern, replace, flags, priority=0,
            case_insensitive=False, context=None):
        """
        Args:
            pattern: A regular expression that matches a string to be replaced.
            replace: The string that the pattern will be replaced with.
            flags: A string of flags to be used in the regular expression.
            priority: An integer that specifies the priority of the mapping.
            case_insensitive: A boolean that specifies whether the mapping is
                case insensitive.
            context: A list of contexts that the mapping applies to.
        """

        self.pattern = pattern
        self.replace = replace
        self.flags = flags
        self.priority
