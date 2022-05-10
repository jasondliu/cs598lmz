import weakref

from . import _base
from . import _compat as _c
from . import _util

from . import _lazy_import as _lim
_lim.lazy_import(globals(), """
import collections
import copy
import decimal
import inspect
import itertools
import operator
import re
import sys
import threading
import time
import types
import warnings

from sqlalchemy import exc as sa_exc
from sqlalchemy import event
from sqlalchemy import log
from sqlalchemy import pool
from sqlalchemy import sql
from sqlalchemy import util
from sqlalchemy.engine import default
from sqlalchemy.engine import reflection
from sqlalchemy.engine import url as sa_url
from sqlalchemy.sql import expression
from sqlalchemy.sql import visitors
from sqlalchemy.sql.elements import ClauseList
from sqlalchemy.sql.expression import literal_column
from sqlalchemy.sql.expression import table
from sqlalchemy.sql.visitors import VisitableType
from sqlalchemy.util import KeyedTuple
from sqlalchemy.util
