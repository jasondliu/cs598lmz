import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)
 
# If the third argument is set to 0, the message box will have the default icon
# If the third argument is set to 1, the message box will have a hand icon
# If the third argument is set to 2, the message box will have a stop icon
# If the third argument is set to 3, the message box will have a question mark icon
# If the third argument is set to 4, the message box will have a exclamation point icon
# If the third argument is set to 5, the message box will have an "i" icon
