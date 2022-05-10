import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_bool)
class _SpellChecker(object):
    '''
    Internal class for spell checking.
    '''
    def __init__(self, dictFile):
        self.lib = ctypes.CDLL(LIB_FILE)
        self.lib.create_spell_checker.restype = ctypes.c_void_p
        self.lib.create_spell_checker.argtypes = [ctypes.c_char_p]
        self.lib.is_word_correct.restype = ctypes.c_bool
        self.lib.is_word_correct.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        self.lib.get_suggestions.restype = ctypes.c_void_p
        self.lib.get_suggestions.argtypes = [ctypes.c_void_p, ctypes.c_char_p, FUNTYPE]
        self.lib.destroy_spell_checker.restype = None
        self.lib.destroy_spell_checker.argtypes
