import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

# import os
# os.system("""osascript -e 'tell app "System Events" to display dialog "Hello World"'""")

# import tkinter as tk
# root = tk.Tk()
# root.withdraw()
# tk.messagebox.showinfo("Hello", "Hello World")

# from win10toast import ToastNotifier

# toaster = ToastNotifier()
# toaster.show_toast("Hello World!!!", "Python is 10 seconds awsm!")

# from win10toast import ToastNotifier
# import time

# toaster = ToastNotifier()
# toaster.show_toast("Hello World!!!",
#                    "Python is 10 seconds awsm!",
#                    icon_path="custom.ico",
#                    duration=10)
# toaster.show_toast("Example two",
#                    "This notification is in it's own thread!",
#                    icon_path=None,
#                    duration=5,

