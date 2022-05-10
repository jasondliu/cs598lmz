import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

#importing modules
import tkinter as tk
import tkinter.messagebox as box
window = tk.Tk()
window.title('Message Box')
tk.Label(window, text='Click button to see a message box.').pack()
def dialog():
    var = box.askyesno('Message Box', 'Proceed?')
    box.showinfo('Returned', var)
tk.Button(window, text='Click', command=dialog).pack()
window.mainloop()

#using lambda to create a function
import tkinter as tk
import tkinter.messagebox as box
window = tk.Tk()
window.title('Message Box')
tk.Label(window, text='Click button to see a message box.').pack()
def dialog():
    var = box.askyesno('Message Box', 'Proceed?')
    box.showinfo('Returned', var)
tk.Button(window, text='Click', command=lambda:dial
