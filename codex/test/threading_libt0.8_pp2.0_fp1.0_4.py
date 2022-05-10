import threading
threading.Thread.daemon = True

# xml file
XML = "examples/news.xml"
xml = etree.parse(XML)

# Create a new Document, append a root node to the document
doc = Document()
root = doc.createElement("news")
doc.appendChild(root)

# get element
for element in xml.iterfind('item'):
    title = element.find('title').text
    link  = element.find('link').text

    # create element
    xml_news = doc.createElement("news_item")
    root.appendChild(xml_news)
    xml_title = doc.createElement("title")
    xml_title.appendChild(doc.createTextNode(title))
    xml_news.appendChild(xml_title)
    xml_link  = doc.createElement("link")
    xml_link.appendChild(doc.createTextNode(link))
    xml_news.appendChild(xml_link)

# save to xml
f = open("examples/news2.xml", 'w')
doc
