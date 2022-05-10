import _struct
import binascii
import struct


class Logger:
    """
    A simple class to mimic the `logging` module.
    """
    def __init__(self, level='info'):
        """
        Logger constructor.

        :param level: level of logging, one of 'debug', 'info', 'warning',
        'error', 'critical'. Defaults to 'info'.
        """
        self.level = level
        self.actual_level = getattr(self, level)

    def debug(self, msg, *args):
        """
        Log debug messages.

        :param msg: message to log.
        :param args: message arguments.
        """
        if self.level == 'debug':
            print('DEBUG:', msg % args)

    def info(self, msg, *args):
        """
        Log info messages.

        :param msg: message to log.
        :param args: message arguments.
        """
        if self.level in ('debug', 'info'):
            print('INFO:', msg % args)

