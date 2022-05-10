import ctypes
import ctypes.util
import threading
import sqlite3

__version__ = '2.2.22'

GANETI_CONFDIR = '/etc/ganeti'
GANETI_RUNDIR = '/var/run/ganeti'
GANETI_QUERY_BINARY = '/usr/bin/gnt-cluster'

# ganeti.2.2.13 or older do not have the --numeric option
if os.path.isfile(GANETI_QUERY_BINARY):
    __cmd_version = subprocess.Popen(GANETI_QUERY_BINARY + ' --version', shell=True, stdout=subprocess.PIPE)
    __version = __cmd_version.stdout.readlines()[0].split()[1]
    ganeti_version = tuple(map(int, __version.split('.')))
    if ganeti_version < (2, 2, 14):
        GANETI_NODE_INFO = '--list'
        GANETI_QUERY = '--list-resources'
        GAN
