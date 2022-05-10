import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_char_p)

#MAX_SEN_LEN = 50

class C_lib:
    def __init__(self):
        self.__lib = ctypes.cdll.LoadLibrary('./lib.so')
        self.__init = self.__lib.init
        self.__init.restype = ctypes.c_void_p
        self.__init.argtypes = None

        self.__destroy = self.__lib.destroy
        self.__destroy.restype = None
        self.__destroy.argtypes = [ctypes.c_void_p]

        self.__add_sentence = self.__lib.add_sentence
        self.__add_sentence.restype = None
        self.__add_sentence.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int]

        self.__build = self.__lib.build
        self.__build.restype = None
        self.__build.argtypes = [ct
