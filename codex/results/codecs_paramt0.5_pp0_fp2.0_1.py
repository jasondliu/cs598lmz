import codecs
codecs.register_error("strict", codecs.ignore_errors)

def parse_args():
    parser = argparse.ArgumentParser(description='Download and parse a Wikipedia dump')
    parser.add_argument('--download', default=False, action='store_true', help='Download a Wikipedia dump')
    parser.add_argument('--parse', default=False, action='store_true', help='Parse a Wikipedia dump')
    parser.add_argument('--dump', default='enwiki-latest-pages-articles.xml.bz2', help='Dump file to download / parse')
    parser.add_argument('--output', default='enwiki-latest-pages-articles.txt', help='Output file to write')
    parser.add_argument('--lang', default='en', help='Language of Wikipedia dump')
    parser.add_argument('--split', default=False, action='store_true', help='Split output into multiple files')
    parser.add_argument('--limit', default=0, type=int, help='Limit the number of articles to parse')
    parser.add_argument('--threads',
