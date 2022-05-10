import bz2
# Test BZ2Decompressor
with bz2.BZ2File('blackwells.xml.bz2', 'r') as xml_file:
    mine = []
    for line in xml_file:
        mine.append(line)

spacey = []
with bz2.BZ2File('bz2_results.txt', 'r') as old_file:
    for line in old_file:
        spacey.append(line)

difference = 0
for i, j in zip(mine, spacey):
    if not i == j:
        print i
        print j
        difference += 1

print difference

print mine[:10]
print spacey[:10]

##print "XML_FILE in BZ2 Encoding"
##print xml_file.read()

#print "Decompress bz2"
print mine

##############test 
#with open('ifd_test.xml','w') as new_file:
#    new_file.write(xml)
