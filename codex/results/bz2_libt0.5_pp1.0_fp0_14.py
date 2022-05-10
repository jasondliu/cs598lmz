import bz2
bz2_file = bz2.BZ2File('wiki.xml.bz2')
xml_file = open('wiki.xml', 'wb')
xml_file.write(bz2_file.read())
xml_file.close()
bz2_file.close()

# Parse the XML file.
import xml.etree.cElementTree as ET
tree = ET.parse('wiki.xml')
root = tree.getroot()

# Create a list of articles.
articles = []
for page in root:
    if page.tag == 'page':
        articles.append(page)

# Parse the articles, and create a dictionary of articles.
articles_dict = {}
for article in articles:
    title = None
    text = None
    for element in article:
        if element.tag == 'title':
            title = element.text
        elif element.tag == 'revision':
            for subelement in element:
                if subelement.tag == 'text':
                    text = subelement.text
    articles_dict[title] = text

#
