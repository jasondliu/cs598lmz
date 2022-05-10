import codecs
codecs.register_error('surrogate_escape', codecs.surrogateescape_error)

import xlrd

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="Location of the Excel file")
parser.add_argument("-s", "--sheet", help="Sheet name")
parser.add_argument("-l", "--label", help="Sheet label")
args = parser.parse_args()

print("Reading file: " + args.file)

# Open the workbook
wb = xlrd.open_workbook(args.file)

print("The number of worksheets is {0}".format(wb.nsheets))
print("Worksheet name(s): {0}".format(wb.sheet_names()))
sh = wb.sheet_by_name(args.sheet)

# List to hold dictionaries
cars_list = []

# Iterate through each row in worksheet and fetch values into dict
for rownum in range(1, sh.nrows):
    cars = Ord
