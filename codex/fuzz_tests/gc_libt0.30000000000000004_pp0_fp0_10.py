import gc, weakref

from . import _gdbmi
from . import _gdbmi_parser

class GdbMi(object):
    def __init__(self):
        self.__parser = _gdbmi_parser.GdbMiParser()
        self.__parser.on_result = self.__on_result
        self.__parser.on_stream_record = self.__on_stream_record
        self.__parser.on_async_record = self.__on_async_record
        self.__parser.on_exec_async_output = self.__on_exec_async_output
        self.__parser.on_status_async_output = self.__on_status_async_output
        self.__parser.on_notify_async_output = self.__on_notify_async_output
        self.__parser.on_unknown_async_output = self.__on_unknown_async_output

        self.__parser.on_error = self.__on_error
        self.__parser.on_warning =
