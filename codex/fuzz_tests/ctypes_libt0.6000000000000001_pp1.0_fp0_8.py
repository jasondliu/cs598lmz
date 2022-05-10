import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)


def callback(event):
    webbrowser.open_new(event.widget.cget("text"))


root = tk.Tk()

label = tk.Label(root, fg="blue", cursor="hand2")
label.pack()
label.bind("<Button-1>", callback)
label.config(text=r"http://www.python.org")

root.mainloop()
