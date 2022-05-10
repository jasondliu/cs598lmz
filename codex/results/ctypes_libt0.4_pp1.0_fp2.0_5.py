import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

# import sys
# import os
# import subprocess
#
# def is_admin():
#     try:
#         return ctypes.windll.shell32.IsUserAnAdmin()
#     except:
#         return False
#
# if is_admin():
#     # Code of your program here
# else:
#     # Re-run the program with admin rights
#     ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

# import os
# import sys
# import subprocess
#
# def is_admin():
#     try:
#         return ctypes.windll.shell32.IsUserAnAdmin()
#     except:
#         return False
#
# if is_admin():
#     # Code of your program here
# else:
#     # Re-run the program with admin rights
#     ctypes.windll.shell32.ShellExecuteW(
