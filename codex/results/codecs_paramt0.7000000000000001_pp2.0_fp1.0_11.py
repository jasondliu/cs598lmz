import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-----------------------------------------------------------------------------
# Module globals
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# General API
#-----------------------------------------------------------------------------

def run(ipy=None, argv=None):
    """Launch a Jupyter QtConsole instance.

    Parameters
    ----------
    ipy : int, optional
        The process ID of the IPython instance to connect to.
    argv : list, optional
        Command line arguments to pass to the QtConsole.  For example, use
        ``argv=['--pylab=inline']`` to start the QtConsole with pylab enabled
        in inline plotting mode.
    """
    if argv is None:
        argv = []

    # Create the application instance.
    app = qt_app.QApplication.instance()
    if app is None:
        app = qt_app.QApplication(argv)

    shell = ZMQTerminalInteractiveShell.instance()

    try:
        import IPython.core.history
        history = IPython.core.history.HistoryManager(shell=
