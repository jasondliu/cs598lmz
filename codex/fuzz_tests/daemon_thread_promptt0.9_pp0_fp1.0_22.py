import threading
# Test threading daemon
import time
import csv
import arcpy
from arcpy import env
env.workspace = r"Z:/Geodatabases/Custom/Resolution_Maps_CSVs.gdb"

# Set open mapping environment

# Import modules
import csv, sys
import Tkinter, tkFileDialog
from Tkinter import *
import os
from os.path import dirname, join
from os import listdir
from os.path import isfile, join
from os import walk
from os.path import normpath, basename
import subprocess
##from shutil import copyfile

# Set workspace for feature classes for field calculations
env.workspace = "Z:/Geodatabases/"


# Create empty lists
csv_list = []
folder_list = []
fl_list = []
one_list = []
two_list = []
three_list = []
four_list = []
five_list = []
six_list = []
fld_list = []
fld_2 = []
fld_3 = []
fld_4 = []
fld_5 =
