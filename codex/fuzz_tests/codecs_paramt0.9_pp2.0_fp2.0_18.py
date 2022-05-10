import codecs
codecs.register_error('xmlcharrefreplace_ignore', lambda e: (u'', e.start + 1))

"""
Methods here are used for rendering xhtml with the asciidoc module.
"""

includexpath="//*[local-name()='includedcontent']"

def includefile(self, content, process, extension):
    """
    Method to include a file, based on the method in xmlwriter.py. This is
    meant to be used with lxml nodes and not just plain-old strings, so that
    encoding on the file object will work and preserve, say, entities.
    
    @param content: uri to file, including query if necessary.
    @param process: expression to select nodes to process.
    @param extension: extension to include in subdocument's generated file.

    @TODO: Allow a user-settable includes directory in the configuration.
    """

    (uri, selector) = split_uri(content)
    doc = self._includefile(uri, extension)
    result = []

    for node in doc.xpath(process, namespaces=get
