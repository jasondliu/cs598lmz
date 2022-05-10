from types import FunctionType
list(FunctionType(lambda x: x+1,globals(),'add_one')(2))

#%%

from os.path import dirname, abspath

DATADIR = dirname(abspath(__file__))
DATAFILE = '../data/beatles-diskography.csv'

def parse_file(datafile):
    data = []
    with open(datafile, 'rb') as f:
        header = f.readline().split(',')
        counter = 0
        for line in f:
            if counter == 10:
                break

            fields = line.split(',')
            entry = {}

            for i, value in enumerate(fields):
                entry[header[i].strip()] = value.strip()

            data.append(entry)
            counter += 1

    return data

print parse_file(DATAFILE)

#%%
import xlrd
datafile = '2013_ERCOT_Hourly_Load_Data.xls'
file_location = dirname(abspath(__file__)) + '/'
