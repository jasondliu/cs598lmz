import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)
# 1=OK, 0=OK/Cancel, 2=Abort/Retry/Ignore, 3=Yes/No/Cancel, 4=Yes/No, 5=Retry/Cancel
# 6=Cancel/Try/Continue, 16=Critical Message Icon, 32=Warning Query Icon, 48=Warning Message Icon, 64=Information Message Icon
# 0=Default Icon, 256=System Modal, 512=Task Modal

# Show a message box:
# ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)
# 1=OK, 0=OK/Cancel, 2=Abort/Retry/Ignore, 3=Yes/No/Cancel, 4=Yes/No, 5=Retry/Cancel
# 6=Cancel/Try/Continue, 16=Critical Message Icon, 32=Warning Query Icon, 48=Warning Message Icon, 64=Information Message Icon
# 0=Default Icon, 256=System Modal, 512=Task Modal


