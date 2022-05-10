import ctypes
ctypes.windll.user32.GetSystemMetrics(0)



# In[9]:


ctypes.windll.user32.GetSystemMetrics(1)


# In[10]:


import tkinter as tk
root = tk.Tk()
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.focus_set() # <-- move focus to this widget
root.bind("<Escape>", lambda e: e.widget.quit())
root.mainloop()


# In[11]:


from tkinter import *
tk = Tk()
tk.title("Test")
frame = Frame(tk, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH,expand=1)
label = Label(frame, text="Hello, World")
label.pack(fill=X, expand=1)
button = Button(frame,text="Exit",command=tk.destroy)
button.pack(side=BOTTOM
