from _struct import Struct
s = Struct.__new__(Struct)
s.wikiextractors = {}


class WikiExtractor(object):

    """
    Extract and clean text from a Wikipedia database dump. Forked from
    https://github.com/attardi/wikiextractor/.

    Each Wikipedia article is processed as an individual document.

    The output is one text file per article, containing the article's
    text, each placed in a directory structure derived from the article's
    title.

    >> WikiExtractor.extract(xmlfile, outfile)

    * `xmlfile` is any bz2 compressed dump file from Wikipedia.
    * `outfile` is a directory.
    * `compress` specifies the compression method used to compress the output files.
    * `debug` turns on debugging information (prints progress information).
    * `processes` specifies the number of concurrent processes.

    """

    def __init__(self, processes=1, html=False, debug=False,
                 no_templates=False, filter_disambig_pages=False):
        self.alltemplates = {}
