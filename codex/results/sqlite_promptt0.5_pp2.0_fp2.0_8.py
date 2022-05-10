import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")
# Test sqlite3.connect("")
# Test sqlite3.connect(None)

from sqlite3 import dbapi2 as sqlite

from sqlite3.test import (dbapi,
                          dbapi2,
                          dbapi2_threadsafety,
                          dbapi2_tpc,
                          dbapi2_tpc_attributes,
                          dbapi2_type_affinity,
                          dbapi2_type_cache,
                          dbapi2_type_collections,
                          dbapi2_type_conversions,
                          dbapi2_type_date,
                          dbapi2_type_datetime,
                          dbapi2_type_decimal,
                          dbapi2_type_factory,
                          dbapi2_type_int,
                          dbapi2_type_iter,
                          dbapi2_type_kwargs,
                          dbapi2_type_null,
                          dbapi2_type_py25,
                          dbapi2_type_row,

