import codecs
codecs.register_error('strict', codecs.ignore_errors)

def unescape(s):
    s = s.replace("&lt;", "<")
    s = s.replace("&gt;", ">")
    # this has to be last:
    s = s.replace("&amp;", "&")
    return s


def get_text(el):
    text = ""
    for node in el.childNodes:
        if node.nodeType == node.TEXT_NODE:
            text = text + node.data
        elif node.nodeType == node.CDATA_SECTION_NODE:
            text = text + node.data
        elif node.nodeType == node.ENTITY_REFERENCE_NODE:
            text = text + node.childNodes[0].data
        elif node.nodeType == node.ELEMENT_NODE:
            text = text + get_text(node)
        else:
            print "unhandled node type: %d" % node.nodeType
    return text


def has_text(el, text):
