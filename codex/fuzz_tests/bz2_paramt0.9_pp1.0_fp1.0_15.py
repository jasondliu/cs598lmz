from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(raw)

#parse
import xml.etree.ElementTree as ET
tree = ET.parse(StringIO(raw))
root = tree.getroot()

#here comes the test tag
for child in root:
    print child.tag, child.attrib
</code>
I've tried to keep your original code pattern, but really, you should probably get used to using <code>urllib.request</code>:
<code>import urllib.request

def main():
    #get a file-like object from the web page
    with urllib.request.urlopen("http://dg.enro.gov.uk/ie/en/feeds/All_Content/rss/today.xml") as rss_file:
        #concatenate all the Strings together
        raw = b"".join(map(bytes, rss_file))

    #parse
    import xml.etree.ElementTree as ET
    tree = ET.parse(StringIO(raw))
    root = tree.getroot()

    #here comes the test tag
   
