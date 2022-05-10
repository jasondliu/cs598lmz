import weakref
from collections import deque
from itertools import count
from logging import getLogger
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

from . import errors
from . import utils
from .utils import (
    _get_node_name,
    _is_node_name,
    _is_node_name_or_node,
    _is_node_or_node_name,
    _is_node_or_node_name_or_node_list,
    _is_node_or_node_name_or_node_list_or_none,
    _is_node_or_node_name_or_node_or_none,
    _is_node_or_node_name_or_node_or_none_or_list,
    _is_node_or_node_name_or_node_or_none_or_list_or_none,
    _is_node_or_node_name_or_node_or_none_or_none,
    _is_node_or_node_
