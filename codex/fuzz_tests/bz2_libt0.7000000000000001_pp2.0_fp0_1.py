import bz2
bz2.BZ2File.read = lambda self, num_bytes = None: self.readline()

# save the original stdout (because we are going to overwrite it)
original_stdout = sys.stdout

# create a file object to accept the redirected stdout
f = open('temp.txt', 'w')

# redirect stdout
sys.stdout = f

# at this point, all output to stdout will go to the file
# create a file-like object to read a zipfile
file = bz2.BZ2File('sample.xml.bz2')

# create a xml parser object
parser = etree.XMLParser(recover=True)

# parse the xml file
tree = etree.parse(file, parser=parser)

# print the xml tree
print(etree.tostring(tree))

# close the file
f.close()

# restore stdout
sys.stdout = original_stdout

# read the contents of the file into a string
with open('temp.txt', 'r') as myfile:

