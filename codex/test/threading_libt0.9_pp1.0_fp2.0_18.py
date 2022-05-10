import threading
threading.stack_size(67108864)

from tkinter import *
import tkinter.messagebox
import math
import random
import time
from fractions import Fraction

root = Tk()
root.title("Bubble sort")
root.geometry('500x500')
root.resizable(False, False)

w = Canvas(root, width=500, height=500)
w.pack()

arr = [50]*50

def go():
    global arr
    maxi = 100
    while True:
        maxi = int(input('\nEnter the number of elements in the array or -1 to stop: '))
        if maxi == -1:
            break
        arr = [random.randint(1, maxi+1) for x in range(maxi)]
        print(arr)
        bubbleSort(arr)

def getColor(col):
    if col == 0:
        col = "#000000"
    if col == 50:
        col = "#FF0000"
