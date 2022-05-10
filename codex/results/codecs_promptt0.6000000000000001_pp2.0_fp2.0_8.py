import codecs
# Test codecs.register_error()
import os
import re
import sys
import textwrap
import unittest
import warnings
from test import support

# The tests are run twice: once with explicit 'strict' errors, and then again
# with 'surrogateescape' error handling enabled.

# One test is run twice: once with bytes input and once with string input.

# One test is run four times: once with each of the three codecs that handle
# surrogates ('utf-8', 'utf-16', and 'utf-32'), and then once for the codec
# that doesn't handle surrogates ('ascii').

# One test is run four times: once with each of the four codecs that handle
# surrogates ('utf-8', 'utf-16', 'utf-32', and 'utf-16-be'), and then once
# for the codec that doesn't handle surrogates ('ascii').

# One test is run eight times: once with each of the eight codecs that handle
# surrogates ('utf-8', 'utf-16', 'utf-32', 'utf-16-be', 'utf-16
