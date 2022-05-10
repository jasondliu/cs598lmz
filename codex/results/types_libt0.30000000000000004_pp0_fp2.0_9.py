import types
types.ClassType = type

import unittest
import os
import sys
import time
import tempfile
import shutil

from test import test_support

# Skip these tests if there is no bsddb module.
test_support.import_module('bsddb')

from bsddb import db
from bsddb.db import DB, DB_HASH, DB_BTREE, DB_RECNO, DB_QUEUE
from bsddb.db import DB_FIRST, DB_NEXT, DB_PREV, DB_LAST, DB_SET_RANGE
from bsddb.db import DB_SET, DB_SET_RECNO, DB_GET_BOTH, DB_GET_BOTH_RANGE
from bsddb.db import DB_JOIN_NOSORT, DB_JOIN_ITEM, DB_JOIN_ITEM_NOSORT
from bsddb.db import DB_DUP, DB_DUPSORT, DB_REVSPLITOFF, DB_RENUMBER
from bsddb.
