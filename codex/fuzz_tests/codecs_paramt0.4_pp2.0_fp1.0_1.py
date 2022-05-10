import codecs
codecs.register_error("strict", codecs.ignore_errors)

# Constants
#
# Default location of the configuration file
DEFAULT_CONFIG_FILE = "/etc/rpki/rpkid.conf"

# Default location of the PID file
DEFAULT_PID_FILE = "/var/run/rpkid.pid"

# Default location of the rpkid log file
DEFAULT_LOG_FILE = "/var/log/rpkid.log"

# Default location of the rpkid log file
DEFAULT_ERROR_LOG_FILE = "/var/log/rpkid.err"

# Default location of the rpkid log file
DEFAULT_TRACE_LOG_FILE = "/var/log/rpkid.trace"

# Default location of the rpkid log file
DEFAULT_DEBUG_LOG_FILE = "/var/log/rpkid.debug"

# Default location of the rpkid log file
DEFAULT_STATUS_LOG_FILE = "/var/log/rpkid.status"

# Default location of the rpkid log file
DE
