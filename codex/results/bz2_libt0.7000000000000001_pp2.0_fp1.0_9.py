import bz2
bz2_file = bz2.BZ2File("wiki.xml.bz2")

import lxml.etree as etree
parser = etree.XMLPullParser(events=("start", "end"))

doc_count = 0

while True:
    data = bz2_file.read(1024)
    if not data:
        break
    parser.feed(data)
    for event, elem in parser.read_events():
        if event == "start" and elem.tag == "doc":
            doc_count += 1
            if doc_count % 10000 == 0:
                print(doc_count)
            doc_id = elem.get("id")
            doc_title = elem.findtext("title")
            doc_text = "".join([elem.text] + [c.text for c in elem.iterchildren()][:-1])

            doc_text_cleaned = doc_text.replace("\\n", "\n").replace("\\t", "\t").replace("\\", "")

            article_page = wikipedia.page
