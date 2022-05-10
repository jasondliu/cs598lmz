import ctypes
ctypes.windll.user32.SystemParametersInfoW(20, 0, r"D:\IMG\Wallpaper\Winter-Night-Sky.jpg", 0)
print("Wallpaper Updated Successfully!")

# Automatically launches Python Shell to run the code

import os
os.startfile("C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python38-32\\python.exe")
