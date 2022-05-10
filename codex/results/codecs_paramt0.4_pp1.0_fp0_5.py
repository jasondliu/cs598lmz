import codecs
codecs.register_error('strict', codecs.ignore_errors)

# Set up the logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Set up the handler
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)

# Set up the formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Add the formatter to the handler
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)


class MyCorpus(object):
    """An interator that yields sentences (lists of str)."""

    def __init__(self, dirname):
        self.dirname = dirname

    def __iter__(self):
        for fname in os.listdir(self.dirname):
            for line in open(os.path.join(self.dirname, fname)):
                yield line.split()


def main():
    # Load
