import mmap
import csv

useless_line = ["--","","U"]

def get_data(file):
    f = open(file)
    mm = mmap.mmap(f.fileno(),0)
    mm = mm.readline()
    mm = mm.decode().split(",")
    return mm

def check_useless_line(line):
    for i in useless_line:
        if i == line:
            return True
        else:
            return False

def check_useless_data(line,i):
    if i==len(useless_line):
        return False
    else:
        if line == useless_line[i]:
            return True
        else:
            return check_useless_data(line,i+1)

def write_to_csv(file):
    csv_file = open(file[:file.rfind(".")+1]+"csv", "w",newline='')
    csv_writer = csv.writer(csv_file)
