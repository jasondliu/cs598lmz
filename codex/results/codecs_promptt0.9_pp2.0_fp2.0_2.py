import codecs
# Test codecs.register_error to deserialize JSON objects
from collections import *
import json
from json import *
# The enum type
import enum
from enum import *  # enum34 backport
from io import *
# The io module is deprecated. Just make it an alias of the io package instead.
# import unittest2 as unittest
# unittest2 is not kept in Python 3.5+
import unittest
from unittest import *
from unittest.util import *


from builtins import *  # NOQA
from unittest import mock


from google.protobuf.pyext import _message
from google.protobuf import _message as pyext_message
from google.protobuf.internal import api_implementation
from google.protobuf.internal import decoder as _decoder
from google.protobuf import message
from google.protobuf.message import Message as _Message
from google.protobuf.internal import type_checkers
from google.protobuf.internal import wire_format
from google.protobuf.internal import well_known_types as _well
