import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")

class Command(threading.Thread):
    def __init__(self, call_stack, cmd, param):
        threading.Thread.__init__(self)
        self.call_stack = call_stack
        self.cmd = cmd
        self.param = param
        self.aes = AESNew()

    def run(self):
        getattr(self, self.cmd)(self.param)

    def __call__(self, *args):
        fun_name = args[0]
        fun_para = tuple(args[1:])
        para_count = fun_para.__len__()
        if para_count == 0:
            self.cmd_write(fun_name + ':')
        if para_count == 1:
            val = str(fun_para[0])
            self.cmd_write(fun_name + ':' + val)
        if para_count == 2:
            val1 = str(fun_para[0])
            val2 = str(fun_para[1])
           
