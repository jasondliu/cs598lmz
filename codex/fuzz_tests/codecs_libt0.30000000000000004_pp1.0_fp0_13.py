import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

# Set up logging
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

# Set up a global variable for the JVM path
jvm_path = jpype.getDefaultJVMPath()

# Start the JVM
jpype.startJVM(jvm_path, "-ea", "-Djava.class.path=stanford-corenlp-full-2018-10-05/*", "-Xmx4g")

# Create a CoreNLP object
nlp = StanfordCoreNLP(r'stanford-corenlp-full-2018-10-05')

# Create a list of stop words
stop_words = stopwords.words('english')

# Create a list of punctuation
punctuations = list(string.punctuation)
