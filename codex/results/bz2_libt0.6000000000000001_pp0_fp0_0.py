import bz2
bz2.open("data/eswiki-20180601-pages-articles-multistream.xml.bz2", "r")

# read in the data
from bz2file import BZ2File
bz2_file = BZ2File("data/eswiki-20180601-pages-articles-multistream.xml.bz2", 'r')

# go through all lines
import xml.etree.ElementTree as ET
for line in bz2_file:
    line = line.decode("utf-8")
    if line.startswith("<page>"):
        # initialize the page
        page = {"id": None, "title": None, "revision": None}
    elif line.startswith("</page>"):
        # process the page
        # print(page)
        pass
    elif line.startswith("</mediawiki>"):
        # finish processing
        break
    else:
        if page["id"] is None:
            # process <id>
            page["id"] = ET.fromstring(line).text

