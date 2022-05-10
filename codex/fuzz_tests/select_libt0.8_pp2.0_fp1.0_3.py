import select

import lib.config.Config as Config
from lib.log.Log import Log
from lib.config.Config import CONFIG


class ConfigdServer(object):
    """
    ConfigdServer class for forking the server process
    """

    LOG_CATEGORY = "configd_server"

    def __init__(self, run_mode):
        self.config_wd_file = os.path.join(
            Config.CONFIG_WORKDIR, "configd_watch_file")
        self.config_wd_file_fd = None
        self.sigterm_received = False
        self.run_mode = run_mode

    def __str__(self):
        return "ConfigdServer"

    def main(self):
        """
        The main function of the daemon
        """
        self.config_wd_file_fd = self.watch_for_clients()
        if self.config_wd_file_fd <= 0:
            sys.exit(1)
        self.set_signal_handlers()
        self.daemonize()

