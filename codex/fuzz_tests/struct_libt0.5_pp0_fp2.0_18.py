import _struct
import _time
import _thread
import _weakref
import _weakrefset
import array
import errno
import fcntl
import itertools
import mmap
import os
import select
import signal
import stat
import sys
import termios
import traceback
import unicodedata
import zlib

from . import _yaml
from . import _yaml_emitter
from . import _yaml_events
from . import _yaml_loader
from . import _yaml_nodes
from . import _yaml_parser
from . import _yaml_reader
from . import _yaml_resolver
from . import _yaml_scanner
from . import _yaml_serializer
from . import _yaml_token
from . import _yaml_writer

__all__ = ['YAML']

_yaml_version = '3.11'

_yaml_file = _yaml_events.Event.from_node(
    _yaml_nodes.MappingNode(
        tag='tag:yaml.org,2002:
