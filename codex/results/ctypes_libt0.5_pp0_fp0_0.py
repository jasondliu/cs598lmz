import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

# https://stackoverflow.com/questions/19078170/showing-message-boxes-in-python-3-3-using-ctypes
# 0 = OK
# 1 = OK | Cancel
# 2 = Abort | Retry | Ignore
# 3 = Yes | No | Cancel
# 4 = Yes | No
# 5 = Retry | No 
# 6 = Cancel | Try Again | Continue

# 0 = Icon Hand
# 16 = Icon Question
# 32 = Icon Exclamation
# 48 = Icon Asterisk

# 0 = Default Button
# 256 = Button 1
# 512 = Button 2
# 768 = Button 3

# 0 = System Modal
# 4096 = Task Modal
