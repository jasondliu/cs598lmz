import mmap

# the config file path
CONFIG_PATH = "config"

# the log file path
LOG_PATH = "log"

# the pid file path
PID_PATH = "pid"

# delete log info when shutdown/reload
LOGGER_LEVEL = logging.ERROR

###############################################################################
# hooks for user defined

def before_fork(signum, frame):
    '''This function will be run before fork'''
    pass

def after_fork(signum, frame):
    '''This function will be run after fork'''
    pass

def before_exit(signum, frame):
    '''This function will be run before exit'''
    pass
