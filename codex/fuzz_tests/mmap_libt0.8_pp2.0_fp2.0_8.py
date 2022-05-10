import mmap
import winsound
import os
'''
import tkinter
from tkinter import ttk
from tkinter.filedialog import askdirectory
'''

#-----------------------------------------------------------------------

#This is the program's main function
if __name__ == '__main__':
    # Bring up the dialog where the user can select a directory
    root = tkinter.Tk()
    root.withdraw()
    currdir = os.getcwd()
    print(currdir)
    tempdir = tkinter.filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
    if len(tempdir) > 0:
        print("You chose %s" % tempdir)

#-----------------------------------------------------------------------

#This allows the program to read through the files with the .pcap extension
    for file in os.listdir(tempdir):
        if file.endswith(".pcap"):
            #print(os.path.join(tempdir, file))
            with open(os.path.join(tempdir
