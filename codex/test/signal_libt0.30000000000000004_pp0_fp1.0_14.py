import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# import the Qt4Agg FigureCanvas object, that binds Figure to
# Qt4Agg backend. It also inherits from QWidget
