import codecs
codecs.register_error('ignore', codecs.decode)


class Indexer(object):
    def __init__(self, wiki, index_path):
        self.wiki = wiki
        self.index_path = index_path

        if not os.path.isdir(self.index_path):
            os.makedirs(self.index_path)

    def run(self, restart=False):
        parse_start = datetime.now()

        print 'starting wiki parsing'
        print

        if not restart:
            try:
                self._parse_raw_xml_dump()

            except IndexError:
                print 'ERROR: could not index the Wikipedia for some reason.'
                print
                print 'It will now delete the half-indexed Wikipedia and start over.'
                print
                print 'If you get this error more than once, check the code, which is probably '
                print 'located at 1-grams/wikipedia/indexer.py'
                print
                print

                shutil.rmtree(self.index_path)
                self._parse_raw_xml_dump()

       
