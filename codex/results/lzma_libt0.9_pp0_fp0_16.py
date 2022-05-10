import lzma
lzma_version = lzma.LZMA_VERSION
if lzma_version < 0x020100:
    raise ImportError(
        "lzma module is outdated %08x (need at least 0x020100)" % lzma_version
    )

from django.db.backends.base.operations import BaseDatabaseOperations
import django.db.backends.utils as utils

try:
    from django.db.backends.sqlite3.base import DatabaseWrapper as DWS3
except ImportError:
    DWS3 = None


class AlterCol:
    def __init__(self, colspec):
        self.colspec = colspec

    def __str__(self):
        return self.colspec


class DatabaseOperations(BaseDatabaseOperations):
    compiler_module = 'django.db.backends.sqlite3.compiler'

    extraction_func = lambda value: value
    no_limit_value = -1

    def autoinc_sql(self, table, column):
        # To simulate auto
