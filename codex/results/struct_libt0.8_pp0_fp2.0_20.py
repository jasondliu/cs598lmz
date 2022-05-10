import _struct

#my imports
import utils


#begin
print("")
print("")
print("")
print("############################################################################")
print("#                                                                          #")
print("#               Script for searching for data                        #")
print("#                                                                          #")
print("############################################################################")
print("")
print("")


#extracts the data from each row and passes it to the callback function
def get_data(table, pointer, callback):

    #open the table
    fp = open(table, "rb")

    #get the table's size
    fp.seek(0,2)
    tablesize = fp.tell()

    #go to the pointer
    fp.seek(pointer)
    
    #search through the table, printing the result of the callback function
    while fp.tell() < tablesize:
        rowsize = fp.read(1)
        if len(rowsize) < 1:
            break
        rowsize = _struct.unpack("B",rowsize)[0]
        row = f
