import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

#MessageBoxA is for ANSI strings
#MessageBoxW is for Unicode strings
#MessageBox is for ANSI strings on Windows 9x/ME and Unicode strings on Windows NT/2000/XP

#MessageBoxA(0, "Your text", "Your title", 1)
#MessageBox(0, "Your text", "Your title", 1)

#The last parameter is the type of buttons and icons you want in your message box.
#The default value for this parameter is 0.
#If you want to display an OK button, you have to set it to 0x00000000L or 0x00001000L.
#If you want to display OK and Cancel buttons, you have to set it to 0x00000001L or 0x00001001L.
#If you want to display Abort, Retry and Ignore buttons, you have to set it to 0x00000002L or 0x00001002L.
#If you want to display Yes, No and Cancel buttons, you have to set it to 0x00000003L or 0x
