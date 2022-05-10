import ctypes
ctypes.windll.shell32.IsUserAnAdmin()

# %%

# import sys
# import os

# if sys.platform.startswith('win'):
#     from ctypes import windll, wintypes
#     from win32com.shell import shell, shellcon

#     def get_special_folder_path(name):
#         if name == 'APPDATA':
#             folder = shell.SHGetFolderPath(0, shellcon.CSIDL_APPDATA, 0, 0)
#         elif name == 'LOCALAPPDATA':
#             folder = shell.SHGetFolderPath(0, shellcon.CSIDL_LOCAL_APPDATA, 0, 0)
#         elif name == 'COMMON_APPDATA':
#             folder = shell.SHGetFolderPath(0, shellcon.CSIDL_COMMON_APPDATA, 0, 0)
#         elif name == 'PROFILE':
#             folder = shell.SHGetFolderPath(0, shellcon.CSIDL_PROFILE, 0, 0)
#
