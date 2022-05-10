from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

# ################################################################################################################################

# ########################################################################
# #### Zato logging functions as used by Zato's own components ############

# ################################################################################################################################

# ########################################################################

import logging
from logging.handlers import TimedRotatingFileHandler
from logging import Formatter

from zato.common.util import get_config_log_format, get_config_log_pattern, get_config_log_size, get_config_log_max_age, get_config_log_max_backups, \
     get_config_log_level, get_config_log_pattern_date, get_config_log_pattern_time, get_config_log_pattern_level, get_config_log_format_date
from zato.common.util import get_config_log_format_time, get_config_log_format_level, get_config_log_format_message

from zato.common.util import ConfigParseException
import
