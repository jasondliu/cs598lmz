import select
import sys
import time

from getpass import getpass

from dnfpluginscore import logger
from dnf.callback import DownloadProgress
from dnf.i18n import _, ucd
from dnf.yum.misc import get_packages_without_source_filenames
from dnf.yum.sqlutils import setup_history_query_limit


class Downloader(object):
    """
    Downloads packages from the repository.
    """

    def __init__(self, base, opts):
        self.base = base
        self.opts = opts
        self.running_threads = 0
        self.progress = None
        self.base.add_metadata_expire_hook(self.download_count_changed)

    def _wait_for_threads(self):
        while self.running_threads > self.opts.max_parallel_downloads:
            time.sleep(0.25)

    def _download_loop(self, pkgs, repos):
        """returns a list of packages which failed
