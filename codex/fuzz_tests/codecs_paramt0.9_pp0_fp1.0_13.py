import codecs
codecs.register_error('strict', codecs.ignore_errors)

class PlainTextExporter(HTMLExporter):
    def __init__(self, fileobj, config=None, **kw):
        self.count = 0
        self.toc = {}
        super(PlainTextExporter, self).__init__(fileobj, config=config, **kw)
    def start_container(self):
        pass
    def end_container(self):
        pass
    def from_markdown(self, source, **kw):
        """Take markdown source string, parse and export as plaintext."""
        self.count +=1
        self.resources = ResourceManager()
        self.output_file = self.file_name.format(count=self.count)
        self.output_extra_file = self.file_name.format(count=self.count)+'.extra'
        self.output_file_extra = codecs.open(self.output_extra_file, 'w+',
                                        encoding='utf-8')
        kw['preamble'] = super(PlainText
