import mmap
import tkinter
from tkinter import *
from tkinter import filedialog, messagebox
from tkinter import *
from tkinter import filedialog, messagebox
from tkinter import ttk


def File_Open():
    fname = filedialog.askopenfilename(filetypes=(("Template files",
                                                    "*.tplate"), ("HTML files", "*.html;*.htm"),
                                                   ("All files", "*.*")))
    if fname:
        try:
            global file
            file = open(fname)
            TextArea.delete(1.0, END)
            TextArea.insert(1.0, file.read())
            file.close()
        except:
            showerror("Open Source File", "Failed to read file\n'%s'" % fname)
        return


def save_file():
    fname = filedialog.asksaveasfilename(defaultextension='.html')
    if fname:
        alltext = TextArea.get(1.0, END)
        open(f
