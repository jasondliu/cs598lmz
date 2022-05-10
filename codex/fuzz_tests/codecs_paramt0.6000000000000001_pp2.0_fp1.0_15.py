import codecs
codecs.register_error("strict", codecs.ignore_errors)

#-------------------------------------------------------------------------------

def get_text(fname):
    with open(fname, "r") as f:
        return f.read()

def get_html(fname):
    with open(fname, "r") as f:
        doc = lxml.html.fromstring(f.read())
        # remove empty paragraphs
        for p in doc.xpath("//p"):
            if not p.text_content().strip():
                p.drop_tree()
        return lxml.html.tostring(doc, encoding='unicode')

def get_title(fname):
    with open(fname, "r") as f:
        doc = lxml.html.fromstring(f.read())
        title = doc.xpath("//h1")[0].text_content()
        return title

def get_authors(fname):
    with open(fname, "r") as f:
        doc = lxml.html.fromstring(f.read())
        authors = doc.
