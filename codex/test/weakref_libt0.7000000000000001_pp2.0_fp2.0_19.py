import weakref

from lib.core.data import conf
from lib.core.data import kb
from lib.core.data import logger
from lib.core.data import queries
from lib.core.exception import SqlmapNotVulnerableException
from lib.core.settings import MSSQL_ALIASES
from lib.core.settings import ORACLE_ALIASES
from lib.core.settings import SQLITE_ALIASES
from lib.core.threads import getCurrentThreadData
from lib.request import inject

def _initBrute():
    """
    Initializes blind SQL injection brute force modules.
    """

    def _setConfAttributes():
        """
        Sets blind SQL injection related configuration attributes.
        """

        conf.db = kb.data.dbms if kb.data.dbms else conf.db
        conf.dbms = kb.data.dbms if kb.data.dbms else conf.dbms

        conf.db = conf.db.lower() if conf.db else ""

