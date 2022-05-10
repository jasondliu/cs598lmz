from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open('/Users/jeannesmits/Downloads/data.bz2', 'rb').read()).decode('latin-1')
#the result of the command is a list
#first item in the list contains the header
#then all data (lines) are in the list with the delimited values being separated by tab
BZ2Decompressor().decompress(open('/Users/jeannesmits/Downloads/data.bz2', 'rb').read()).decode('latin-1').split("\n")[0:4]
#from the header we need to know how many entries we need
#there are 18 variables and the last 3 are part of the country name
#so we need 15 entries
#various possibilities to create a list and store the data in a data structure
#this is a nested list and each list represents a row/data point
#to access a value you would use a double index
#data[5][0] would give you the first value of the 6th list
#data[5][1] would give you the second value of the 6th list
#
