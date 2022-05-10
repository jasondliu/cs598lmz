import gc, weakref
import sys

from django.db import connection
from django.utils import six

from debug_toolbar.panels import DebugPanel
from debug_toolbar.utils import sqlparse, tidy_stacktrace, format_sql
from debug_toolbar.utils.tracking import replace_call

# SQL generation can be slow. Disable SQL generation if the view executed
# less than this amount of SQL statements.
DISABLE_SQL_GENERATION_THRESHOLD = 1000

# Mutex for disabling SQL generation
disable_sql_generation_lock = threading.Lock()

# The following code is a copy of django.db.backends.util.CursorDebugWrapper
# for Django < 1.6.
#
# The reason is that the CursorDebugWrapper class has been moved to private
# API in Django 1.6.  Instead of copying the whole class, we wrap the
# connection cursor (which is now a private API too) and delegate to it.
#
# This code can be removed when support for Django < 1.6 is dropped.


class CursorDebugWrapper(object):
