import codecs
codecs.register_error('replace_python2',
            lambda e: (u"\ufffd", e.start + 1))


from configobj import ConfigObj
from lib.core.enums import RESULTS_STATE_IDS
from lib.core.common import parseTargetDirect, autocomplete
from lib.core.threads import getCurrentThreadData
from lib.core.threads import getCurrentThreadData
from lib.core.exception import SqlmapFilePathException
from lib.core.settings import IS_WIN
from lib.core.settings import LEGAL_DISCLAIMER
from lib.core.settings import VERSION_STRING
from lib.core.settings import ISSUES_PAGE
from lib.core.settings import WIKI_URL
from lib.core.settings import MANUAL_URL
from lib.core.settings import TRANSFERS_THREAD_POLL_FREQ
from lib.core.settings import TRANSFERS_THREAD_KILL_SLEEP_TIME
from lib.core.settings import SEPARATOR
from lib.core.settings import TIME_DELAY_CANDIDATES
from lib
