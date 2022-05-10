import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)
 
#The first parameter is the parent window handle, the second is the text, 
#the third is the title and the last one is the type of the message box. 
#The last one is optional and if you don't set it, it will show an "OK" button.
#
#The types are as follows:
#
#0 : OK
#1 : OK | Cancel
#2 : Abort | Retry | Ignore
#3 : Yes | No | Cancel
#4 : Yes | No
#5 : Retry | No 
#6 : Cancel | Try Again | Continue
#
#and for question mark icon you can set the type as 0x20 and for exclamation point as 0x30.



import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 0x30)
