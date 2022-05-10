import types
types.ModuleType('__builtin__').sys.stdout.write = lambda x: x

#
# "html" formatter
#

def htmlfmt(env, node, status, docname):
    import xhtmlwriter
    from HTMLParser import HTMLParser
    xhtml = xhtmlwriter.XHTMLWriter(HTMLParser())
    xhtml.enter('class=document')
    xhtml.enter('class=section level=1')
    xhtml.write('<b class="title">%s</b>' % \
                env.fs.get_titles()[node.name])
    xhtml.leave() # section
    xhtml.write('<div class="body">')
    xhtml.write(env.fs.get_body(node.name))
    xhtml.leave() # body
    xhtml.leave() # document
    return xhtml.get()

#
# "download" formatter
#

def downloadfmt(env, node, status, docname):
    import xhtmlwriter
    from HTMLParser import HTMLParser
