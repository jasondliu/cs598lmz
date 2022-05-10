import mmap
import os
import re
import sys
import tempfile
import textwrap
import unittest

from six.moves import builtins

try:
    from unittest import mock
except ImportError:
    import mock

import modernize

