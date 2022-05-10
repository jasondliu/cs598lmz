import ctypes
ctypes.windll.user32.LockWorkStation()
os.system('shutdown -s')
