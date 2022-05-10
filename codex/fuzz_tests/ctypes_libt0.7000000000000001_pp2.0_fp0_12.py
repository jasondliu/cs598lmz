import ctypes
ctypes.windll.shell32.IsUserAnAdmin()

# win32com.shell.shell.IsUserAnAdmin()
if ctypes.windll.shell32.IsUserAnAdmin():
    print("You are an admin!")
else:
    print("You are not an admin!")

os.system("pause")
