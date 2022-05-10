import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

#import ctypes
#ctypes.windll.user32.MessageBoxA(0, "Your text", "Your title", 1)

#import ctypes
#ctypes.windll.user32.MessageBoxA(0, "Your text".encode('utf-8'), "Your title".encode('utf-8'), 1)

import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text".encode('utf-8').decode('utf-8'), "Your title".encode('utf-8').decode('utf-8'), 1)

#import ctypes
#ctypes.windll.user32.MessageBoxW(0, u"Your text".encode('utf-8').decode('utf-8'), u"Your title".encode('utf-8').decode('utf-8'), 1)

#import ctypes
#ctypes.windll.user32.MessageBoxA(0, u"Your text", u"Your
