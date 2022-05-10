import socket
import _thread
import tkinter
import pickle
import time
import json
import hashlib as hasher

# variables for the GUI

window = tkinter.Tk()
window.geometry("500x500")
window.title("Blockchain GUI")

scrollbar = tkinter.Scrollbar(window)
input_textbox = tkinter.Text(window, height=9, width=83)
output_text_box = tkinter.Text(window, height=22, width=82)
scrollbar.pack(side=tkinter.RIGHT, fill = tkinter.Y)
input_textbox.pack(side = tkinter.LEFT, fill = tkinter.Y)
output_text_box.pack(side = tkinter.LEFT, fill = tkinter.Y)
input_textbox.pack(side=tkinter.TOP, fill=tkinter.Y)
output_text_box.pack(side=tkinter.BOTTOM, fill=tkinter.Y)
