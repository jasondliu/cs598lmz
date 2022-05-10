import ctypes
ctypes.cast(foo, ctypes.c_void_p).value = bar

# set the tkinter font such that shorter text will fit
# http://www.blog.pythonlibrary.org/2017/07/26/tkinter-how-to-show-all-characters-in-a-ttk-combobox/

def change_dropdown_font_size(widget, new_size):
    widget.style.map("TCombobox", fieldbackground=[("readonly","white")],
                                                foreground=[("readonly","black")])
    widget.style.map("TCombobox", selectbackground=[("readonly","blue")],
                                                  selectforeground=[("readonly","white")])
    widget.style.map("TCombobox", background=[("readonly","white")])
    widget.configure(style="TCombobox")
    widget.option_add("*TCombobox*Listbox.font", ("TkDefaultFont", new_size))
    widget.option_add("*TCombobox*Listbox*Font", ("TkDefaultFont",
