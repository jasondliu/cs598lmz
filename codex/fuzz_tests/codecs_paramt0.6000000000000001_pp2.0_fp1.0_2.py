import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

# setup the log file
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def read_input(file):
    """This method reads the input file which is in gzip format"""

    logging.info("reading file {0}...this may take a while".format(file))
    with open(file, 'rb') as f:
        for i, line in enumerate(f):
            logging.info("read {0} reviews".format(i))
            # do some pre-processing and return a list of words for each review text
            yield gensim.utils.simple_preprocess(line)


# read the tokenized reviews into a list
# each review item becomes a serries of words
# so this becomes a list of lists
documents = list(read_input(data_file))
logging.info("Done reading data file")

# build vocabulary and train model
model = gensim.models.Word
