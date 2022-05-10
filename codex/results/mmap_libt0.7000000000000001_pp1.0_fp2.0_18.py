import mmap
from datetime import datetime
from datetime import timedelta
import os
import shutil
from os import listdir
from os.path import isfile, join
import sys
import string
import re

# import the class
from Scanner import Scanner

# Set the path for the csv file to be output
output_path = sys.argv[1]
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, output_path)

# Set the path for the file to be used as a dictionary
dict_path = sys.argv[2]
my_path2 = os.path.abspath(os.path.dirname(__file__))
path2 = os.path.join(my_path2, dict_path)

# Create an instance of the class and pass in the path for the file to be used as a dictionary
s = Scanner(path2)

# pass the path for the output csv file
path = s.create_csv(path)

#
