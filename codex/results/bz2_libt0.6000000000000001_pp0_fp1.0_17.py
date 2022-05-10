import bz2
bz2.BZ2File

# open the file
f = bz2.BZ2File('data/wiki.xml.bz2', 'r')

# read the entire file
xml = f.read()
#print(type(xml))

# close the file
f.close()

# parse the xml file
print('Parsing xml')
tree = ET.fromstring(xml)

# get root node
root = tree.getroot()

# print the first child tag
print(root[0].tag)

# print the first child's attributes
print(root[0].attrib)

# print all (grand)children of the first child
for grandchild in root[0]:
    print(grandchild.tag)


# create empty lists for title and text
titles = []
texts = []

# iterate over all revisions in the xml file
for i, page in enumerate(root):
    # print(page.tag)
    # print(page.attrib)
    if i % 10000 == 0:
        print('Processing revision {}'.
