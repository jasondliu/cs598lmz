import mmap
from os.path import join, getsize
from time import time
from threading import Thread
#from multiprocessing import Process
from Queue import Queue, Empty
from gzip import GzipFile
from bz2 import BZ2File

from . import const
from .util import is_valid_file, logger, create_zip_archive, Archiver, \
    create_tar_archive, create_7z_archive
from .account import Account
from .error import AccountNotFound, AccountExists
from .db_accounts import DBAccounts


class BackupManager(object):
    """
    Backup manager is used to manage backups. The only object of this class
    should be created globally, since only one backup can be performed at the
    time.
    """

    def __init__(self, db_accounts, db_settings, db_backups, backup_address,
                 dump_backup_address, logger, backup_log_path, db_mode,
                 backup_max_interval, backup_max_age):
        if not db_accounts:
           
