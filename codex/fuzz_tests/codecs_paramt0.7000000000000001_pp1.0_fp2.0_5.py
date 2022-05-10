import codecs
codecs.register_error("strict", codecs.ignore_errors)

# csv file write
import csv
# sys.stdout = codecs.getwriter("sjis")(sys.stdout)
import pprint
import os
import glob
import datetime


print("start :",datetime.datetime.now())

print("open file ")

file_list = glob.glob("./cell_log/Z_*.csv")
csv_file = codecs.open("./cell_log/Z_cell_log.csv", "w", "SJIS")
# csv_file = codecs.open("./cell_log/Z_cell_log.csv", "w", "cp932")

# csv_file = codecs.open("./cell_log/Z_cell_log.csv", "w", "utf-8")

# csv_file = codecs.open("./cell_log/Z_cell_log.csv", "w", "utf-8")

# csv_file = codecs.open("./cell
