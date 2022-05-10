import codecs
codecs.register_error('strict', codecs.ignore_errors)

from . import __version__
from . import config
from . import utils
from . import log
from . import exceptions
from . import commands
from . import cache
from . import commands_cache
from . import commands_help
from . import commands_init
from . import commands_list
from . import commands_run
from . import commands_search
from . import commands_show
from . import commands_update
from . import commands_version
from . import commands_which
from . import commands_zap
from . import commands_zap_all
from . import commands_zap_cache
from . import commands_zap_config
from . import commands_zap_log
from . import commands_zap_run
from . import commands_zap_search
from . import commands_zap_show
from . import commands_zap_update
from . import commands_zap_which
from . import commands_zap_zap
from . import commands_zap_zap_all
from . import commands_zap_zap_cache

