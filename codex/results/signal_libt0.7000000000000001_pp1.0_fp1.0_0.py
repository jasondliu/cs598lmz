import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

def _set_user_home(path):
    from gns3.qt import QtCore
    if not path.endswith("/"):
        path = "{}/".format(path)
    if not os.path.exists(path):
        os.makedirs(path)
    QtCore.QDir.setCurrent(path)


def _setup_logging(home=None, debug_mode=False, log_file=None, log_to_stdout=True):
    import logging
    import logging.handlers
    """
    Setup logging
    """
    # create console logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    if debug_mode is False:
        logger.setLevel(logging.INFO)

    # create a rotating file handler
    if log_file and home:
        log_file = os.path.join(home, log_file)
    else:
        log_file = None

    if
