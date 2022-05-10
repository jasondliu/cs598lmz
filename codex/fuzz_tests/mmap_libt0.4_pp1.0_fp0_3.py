import mmap
import sys
import os
import re
import time
import signal

# Global variables

# The name of the file that contains the list of processes to monitor
process_file = '/etc/process_checker/processes'

# The name of the file that contains the list of processes to ignore
ignore_file = '/etc/process_checker/ignore'

# The name of the file that contains the list of processes to monitor
# that are not running as root
non_root_file = '/etc/process_checker/non_root'

# The name of the file that contains the list of processes to monitor
# that are running as root
root_file = '/etc/process_checker/root'

# The name of the log file
log_file = '/var/log/process_checker.log'

# The name of the pid file
pid_file = '/var/run/process_checker.pid'

# The name of the lock file
lock_file = '/var/lock/process_checker.lock'

# The name of the file that contains the list of
