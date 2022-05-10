import weakref
import resource
import traceback

import isc.log
import isc.cc.data
import isc.cc.session
import isc.cc.bind10
import isc.cc.server
import isc.config.utils

class Server(object):
    """The cc_server class"""

    def __init__(self, cfg_file, bind10_setup=None, server_setup=None,
                 stats_backend=None, data_sources=None,
                 logger_file=None, logger_name=None, logger_type="default"):

        # the configuration filename
        self.__cfg_file = cfg_file

        # the file path of the log
        self.__log_file = logger_file

        # the name used in the logger
        self.__log_name = logger_name

        # the logger type
        self.__log_type = logger_type

        # the logger
        self.__logger = isc.log.create_logger(logger_file=self.__log_file,
                                              logger_
