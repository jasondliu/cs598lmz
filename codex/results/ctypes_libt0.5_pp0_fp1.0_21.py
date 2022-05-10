import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

#import win32api
#win32api.MessageBox(0, 'Message', 'Title')

#import win32gui
#def alert(title, text):
#    win32gui.MessageBox(0, text, title, 0x00001000) #MB_ICONINFORMATION)
#alert("Title", "Message")

#import tkinter as tk
#root = tk.Tk()
#root.withdraw()
#tk.messagebox.showinfo("Title", "Message")


#import tkinter as tk
#root = tk.Tk()
#root.withdraw()
#tk.messagebox.showerror("Title", "Message")

#import tkinter as tk
#root = tk.Tk()
#root.withdraw()
#tk.messagebox.showwarning("Title", "Message")

#import tkinter as tk
#root = tk.Tk()
#root.withdraw()

