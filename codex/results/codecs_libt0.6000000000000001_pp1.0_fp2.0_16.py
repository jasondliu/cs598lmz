import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# for writing to excel file
from xlwt import Workbook

# for writing to csv file
import csv

# for generating the pdf
import pdfkit

# for randomizing the list of people
import random

# for finding the current date
from datetime import datetime

# for notifying the user
import winsound


#-------FUNCTIONS-------#

# function to read in the data (from an excel file)
def read_excel(file_name):
    wb = xlrd.open_workbook(file_name)
    sheet = wb.sheet_by_index(0)
    return sheet

# function to generate the list of people
def generate_list_of_people(sheet):
    list_of_people = []
    for i in range(2, sheet.nrows):
        list_of_people.append(sheet.cell_value(i, 0))
    return list_of_people

#
