import ctypes
ctypes.windll.user32.MessageBoxA(0, "Your text", "Your title", 1)

import webbrowser
webbrowser.open_new_tab('https://www.python.org/')

youtube_url = 'https://www.youtube.com/watch?v=YpYBvv0Rg8o'
webbrowser.open_new_tab(youtube_url)

from tkinter import messagebox
messagebox.showinfo('Message title', 'Message content')

messagebox.showwarning('Message title', 'Message content')

messagebox.showerror('Message title', 'Message content')

answer = messagebox.askyesno('Message title', 'Message content')

answer = messagebox.askokcancel('Message title', 'Message content')

answer = messagebox.askquestion('Message title', 'Message content')

answer = messagebox.askretrycancel('Message title', 'Message content')

answer = messagebox.askyesnocancel('Message title', 'Message content')

from tkinter import simpledialog
answer
