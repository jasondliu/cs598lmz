import codecs
codecs.register_error("strict", codecs.ignore_errors)

LANG_LABEL_RE = re.compile("""<label xml:lang="([^"]+)">([^<]*)</label>""")
TITLE_RE = re.compile("""<title>([^<]*)</title>""")

GRAPH_RE = re.compile("<graph>")

# A graph, along with a title and language label
GRAPH_HEADER_RE = re.compile("""<graph>\s*(.*)""")

# A graph, along with a title and language label
GRAPH_RE = re.compile("""<graph>\s*(.*)%(:title)s(.*)%(:label)s(.*)""" %
                      {":title": TITLE_RE.pattern,
                       ":label": LANG_LABEL_RE.pattern})

GRAPH_FOOTER_RE = re.compile("</graph>")

def parse_graph_label(label):
    """
    Return a tuple (
