import codecs
codecs.register_error('strict', codecs.ignore_errors)

from . import __version__
from . import __author__
from . import __url__
from . import __license__
from . import __doc__

from . import config
from . import data
from . import util
from . import log
from . import exceptions
from . import plugins
from . import commands
from . import commands_help
from . import commands_plugins
from . import commands_config
from . import commands_data
from . import commands_util
from . import commands_log
from . import commands_exceptions
from . import commands_version
from . import commands_help
from . import commands_test
from . import commands_template
from . import commands_init
from . import commands_run
from . import commands_run_test
from . import commands_run_template
from . import commands_run_init
from . import commands_run_run
from . import commands_run_config
from . import commands_run_data
from . import commands_run_util
from . import commands_run_log
from . import commands_run_ex
