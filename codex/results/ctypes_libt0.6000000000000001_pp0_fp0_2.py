import ctypes
ctypes.windll.user32.MessageBoxA(0, "Your text", "Your title", 1)

#you can also import messagebox
import tkinter.messagebox
tkinter.messagebox.showinfo("Title", "a Tk MessageBox")

#ask question
import tkinter.messagebox
tkinter.messagebox.askquestion("Question 1", "Do you like silly faces?")

#ask question
import tkinter.messagebox
response = tkinter.messagebox.askquestion("Question 1", "Do you like silly faces?")

#if answer is yes
import tkinter.messagebox
response = tkinter.messagebox.askquestion("Question 1", "Do you like silly faces?")

if response == 'yes':
    print(" 8===D~ ")

#if answer is no
import tkinter.messagebox
response = tkinter.messagebox.askquestion("Question 1", "Do you like silly faces?")

if response == 'no':
    print(" :( ")

#import class
from tkinter import filedialog

