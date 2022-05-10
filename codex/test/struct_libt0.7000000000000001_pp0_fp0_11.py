import _struct

from . import util
from . import support
from . import variables
from . import exceptions
from . import connection
from . import extensions
from . import sqltypes
from . import processors


log = logging.getLogger(__name__)


class DefaultDialect(object):
    name = None
    driver = None
    supports_sane_rowcount = True
    supports_sane_multi_rowcount = True
    supports_unicode_statements = True
    supports_unicode_binds = True
    default_paramstyle = 'qmark'

    colspecs = {}

    statement_compiler = None
    ddl_compiler = None
    type_compiler = None
    ischema_names = None
    preparer = None
    supports_alter = True
    supports_pk_autoincrement = True
    supports_default_values = True
    supports_empty_insert = False
    supports_multivalues_insert = False
    supports_sequence_reset = True
