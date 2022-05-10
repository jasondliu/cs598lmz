import bz2
bz2file = bz2.BZ2File('output/rcgcorpus.json.bz2', 'w', compresslevel=9)
bz2file.write(string)
bz2file.close()
zipfile = zipfile.ZipFile('output/rcgcorpus.json.zip', 'w', zipfile.ZIP_DEFLATED)
zipfile.write('output/rcgcorpus.json', 'rcgcorpus.json')
zipfile.close()
print len(string)

# close(sequence)

# serialize(tree, 'output/rcg.xml')
# print 'Parsing time: ' + str(time.clock() - t)
