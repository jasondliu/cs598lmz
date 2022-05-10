import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)

#to open pdf file of the chart
from PyPDF2 import PdfFileReader
#to recognize the text in the chart
from pdf2image import convert_from_path
from pytesseract import image_to_string

#to get the time
from datetime import time

#creating a window using tkinter
window=Tk()
window.geometry('800x600')
window.title('Chore Chart')
window.configure(bg='blue')

#creating a frame
frame=Frame(window)
frame.pack()

#creating a frame for the title
frame1=Frame(window, bg='white')
frame1.pack(side=TOP)

#creating a frame for the labels
frame2=Frame(window, bg='white')
frame2.pack(side=TOP)

#creating a frame for the buttons
frame3=Frame(window, bg='white')
frame3.pack(side=TOP)

#creating a frame for the
