import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)


class CmdLine(object):
    def __init__(self):
        parser = argparse.ArgumentParser(description='Generate a text file with the list of all the files in a folder and its subfolders')
        parser.add_argument('-i', '--input', dest='input', required=True, help='Input folder')
        parser.add_argument('-o', '--output', dest='output', required=True, help='Output file')
        #parser.add_argument('-l', '--list', dest='list', action='store_true', help='List all the files')
        parser.add_argument('-v', '--verbose', dest='verbose', action='store_true', help='Verbose')
        #parser.add_argument('-d', '--debug', dest='debug', action='store_true', help='Debug')
        self.args = parser.parse_args()


def list_files(path, verbose):
