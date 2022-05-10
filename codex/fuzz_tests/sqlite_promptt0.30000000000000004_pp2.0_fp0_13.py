import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared', uri=True)

import pytest

from . import util
from . import dbapi2
from . import types
from . import userfunctions
from . import complete_statement
from . import complete_one_statement
from . import complete_partial_statement
from . import complete_partial_statement_with_limit
from . import complete_partial_statement_with_limit_and_offset
from . import complete_partial_statement_with_limit_and_offset_and_order_by
from . import complete_partial_statement_with_limit_and_offset_and_order_by_and_group_by
from . import complete_partial_statement_with_limit_and_offset_and_order_by_and_group_by_and_having
from . import complete_partial_statement_with_limit_and_offset_and_order_by_and_group_by_and_having_and_where
from . import complete_partial_statement_with_limit_and_offset_and_order_by_and_group_by_and_having
