import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)


class GetReverseCurrent(object):
    def __init__(self, dll):
        self.mydll = dll
        self.mydll.set_get_reverse_current_calback(FUNTYPE(self.get_reverse_current_calback))

    def get_reverse_current_calback(self):
        """
        This function shall be called from the DLL to get the current value of the reverse stock
        :return:
        """
        print('In GetReverseCurrent.get_reverse_current_calback')
        return ctypes.c_int(42).value
