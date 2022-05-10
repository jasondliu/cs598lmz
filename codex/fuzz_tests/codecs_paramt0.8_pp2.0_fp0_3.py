import codecs
codecs.register_error("xmlcharrefreplace", lambda exc: (u"&#%d;" % exc.end, exc.end+1))


class XmlGenerator(object):
    def __init__(self, file, indentation):
        self.current_indent = 0
        self.indentation = indentation
        self.file = file

    def indent(self):
        self.current_indent += 1

    def dedent(self):
        if self.current_indent <= 0:
            raise ValueError("Indentation error")
        self.current_indent -= 1

    def write(self, text):
        self.file.write("  " * self.current_indent)
        self.file.write(text)

    def writeln(self, text=""):
        self.write(text)
        self.file.write("\n")

    def write_tag_head(self, tag, attributes={}):
        self.write("<%s" % tag)
        for attribute in attributes:
            self.write(" %s=\"%s\"" % (
