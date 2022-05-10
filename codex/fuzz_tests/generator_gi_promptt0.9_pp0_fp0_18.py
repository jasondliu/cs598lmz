gi = (i for i in ())
# Test gi.gi_code

# Test data type of generator
from types import GeneratorType

# Test code objects
import types

# Test code co_consts
from types import CodeType

# Test pattern match
from re import compile

# Test pattern match
from struct import pack


# Test the stack overflow protection
from exceptions import MemoryError


# Test stack frames

# Test .pyc files
import sys
from tempfile import gettempdir


if sys.version_info[0] < 3:
    from new import function

# Test dict objects

from types import DictType

# Test code co_consts
from types import CodeType

import sys

from os import unlink

from marshal import loads
from types import CodeType


from os import environ

def test_frompyfile():
    """from_pyfile function tests"""

    filename = os.path.join(os.path.dirname(__file__), 'test_config')

    g = Config(dict(
        DEBUG=True,
        SECRET_KEY='development key',
        USERNAME='admin
