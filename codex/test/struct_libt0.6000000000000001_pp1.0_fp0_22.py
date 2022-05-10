import _struct

from . import _compat as _b
from . import _compat
from . import _errors
from . import _types


_logger = logging.getLogger(__name__)


def _get_types_module(db):
    """Get the types module for a given database."""
    if db == "psycopg2":
        return psycopg2.extensions
    elif db == "psycopg2-binary":
        return psycopg2.extensions
    elif db == "psycopg2cffi":
        return psycopg2cffi.extensions
    elif db == "pg8000":
        return pg8000.types
    elif db == "mysql-connector-python":
        return mysql.connector.django.base
    elif db == "mysqlclient":
        return MySQLdb.converters
    elif db == "pymysql":
        return pymysql.converters
    elif db == "sqlite3":
        return sqlite3
