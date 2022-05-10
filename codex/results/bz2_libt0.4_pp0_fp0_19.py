import bz2
bz2file = bz2.BZ2File('/Users/jason.katz/Downloads/enwiki-latest-pages-articles-multistream.xml.bz2')

import xml.etree.ElementTree as ET

def get_pages(bz2file):
    """
    Generator that yields pages from the Wikipedia dump.
    """
    current_page = []
    for line in bz2file:
        line = line.decode("utf-8")
        if line.startswith("<page>"):
            current_page = [line]
        elif line.startswith("</page>"):
            current_page.append(line)
            yield "".join(current_page)
        else:
            current_page.append(line)

def get_text_from_page(page):
    """
    Parses an XML page from the Wikipedia dump and returns the text.
    """
    root = ET.fromstring(page)
    text = root.find("revision/text").text
    title = root.find("title").text
