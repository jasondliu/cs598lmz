import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)
sys.exit(0)
'''

'''
notification
'''
'''
from win10toast import ToastNotifier
toaster = ToastNotifier()
toaster.show_toast("Example two", "This notification is in it's own thread! :)", duration=5)

# Wait for threaded notification to finish
while toaster.notification_active(): time.sleep(0.1)
'''



'''
os.system("notepad.exe")
'''

'''
import os

# os.startfile('c:\\Users\\shani\\Desktop\\tests\\test.txt')

# print(os.getcwd())

os.chdir("D:\\Shani\\Python\\Python-VScode-Auto-edit\\test1")

print(os.listdir("."))

print(os.getcwd())

# os.makedirs("D:\\Shani\\Python\\Python-VScode-Auto-
