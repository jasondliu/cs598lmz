import bz2
bz2.BZ2File("./enwiki-latest-pages-articles.xml.bz2")

#import xml.etree.ElementTree as ET
#tree = ET.parse("./enwiki-latest-pages-articles.xml")
#root = tree.getroot()
#for child in root:
#    print(child.tag, child.attrib)
#print(root.tag)

#from xml.etree.ElementTree import iterparse
#for event, elem in iterparse("./enwiki-latest-pages-articles.xml"):
#    print(event, elem.tag)
    
#from xml.etree.ElementTree import iterparse
#for event, elem in iterparse("./enwiki-latest-pages-articles.xml"):
#    if event == "end" and elem.tag == "text":
#        print(elem.text)
#        elem.clear()

#from xml.etree.ElementTree import iterparse
#def parse_and_remove(filename, path):
#    path_parts
