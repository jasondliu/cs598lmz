import bz2
bz2.
%paste
 

binary_file_name = r'C:\Users\alber\Desktop\Projects\biomajor\Sarath\Bifidobacterium.fasta.bz2'

file1 = open(binary_file_name, "r")

file1 = bz2.BZ2File(binary_file_name)

output = open('decompressed.fasta', 'wb')
output.write(file1.read())
output.close()
file1.close()

# *********************************************************************************#
# *********************************************************************************#


# Parse fasta file and extract the taxid at the end of the description line 
import re

openfile = open("C:/Users/alber/Desktop/Projects/biomajor/Sarath/Sarath/Sarath/Bifidobacterium.fasta").readlines()

# for i in openfile:
#     print (i)

# regex filtering
for i in openfile:
    if re.match(">|gi", i):
        tax_
