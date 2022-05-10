import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_void_p)    
MF_CHECKED = -1 
MF_UNCHECKED = 0
# pywintypes.error # 1223

# MENU ITEM/ITEMINFO FLAGS: https://docs.microsoft.com/en-us/windows/win32/menurc/menuiteminfo
MIIM_ID = 0x00000002
MIIM_STRING = 0x000000040
MIIM_BITMAP = 0x00000080


class Monitor:
    def __init__(self):
        super().__init__()
        self.stop_thread_flag=threading.Event()
        self.thread = None
        self.menucmds = None
        self.language = 'en-US'
        self.GetLangID()
    
    
    def GetLangID(self):
        langid = ctypes.windll.kernel32.GetUserDefaultUILanguage()
        self.language = [langid & 0xff, (langid >> 8) & 0xff]


    def CheckAdditions(self, event=None
