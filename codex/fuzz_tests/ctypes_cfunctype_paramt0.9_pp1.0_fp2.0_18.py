import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
order = {
    "eq": 0,
    "leq": 1,
    "geq": 2,
}


def set_log_level(level):
    clp_logger = CLPLogger.get_instance()
    clp_logger.set_log_level(level)


class CLPLogger(Logger):
    """
    CLP logger performs logging for CLP.
    """

    __CLP_LOGGER_SINGLETON = None

    def set_log_level(self, level):
        if level == "debug":
            self.log_to_silent()
            create_clp_callback(CLPLogger.debug_clp_callback)
        elif level == "info":
            self.log_to_stdout()
            create_clp_callback(CLPLogger.info_clp_callback)
        elif level == "error":
            self.log_to_stderr()
            create_clp_callback(CL
