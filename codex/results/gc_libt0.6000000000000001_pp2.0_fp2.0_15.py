import gc, weakref, os
from types import ModuleType

try:
    from Tkinter import Tk
    from idlelib import PyShell
    from idlelib.EditorWindow import EditorWindow
    from idlelib.FileList import FileList
    from idlelib.configHandler import idleConf
    from idlelib.configHandler import idleConf
    from idlelib.configSectionNameDialog import ConfigSectionNameDialog
    from idlelib.configSectionNameDialog import GetCfgSectionNameDialog
    from idlelib.configHelpSourceEdit import ConfigHelpSourceEdit
    from idlelib.configHelpSourceEdit import GetCfgSectionHelpSourceEdit
    from idlelib.configDialog import ConfigDialog
    from idlelib.configDialog import GetCfgSectionNameDialog
    from idlelib.configDialog import GetCfgSectionKeys
    from idlelib.configDialog import GetCfgKeys
    from idlelib.configDialog import GetAllExtraHelpSourcesList
    from idlelib.configDialog import GetExtraHelpSourceList
    from idlelib.configDialog import GetUserCfgFilename
    from idlelib.configDialog import GetGlobalCfgFilename
    from idlelib.config
