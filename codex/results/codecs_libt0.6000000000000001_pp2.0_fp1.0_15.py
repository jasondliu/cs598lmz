import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# Logging
if __name__ == '__main__':
    log = logging.getLogger('isr')
    log.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    # add the handlers to the logger
    log.addHandler(ch)
else:
    log = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description='Analyze a given file or directory of files.')
    parser.add_argument('--dir', nargs='?', help='Directory to analyze.')
    parser.add_argument('--file', nargs='?', help='File
