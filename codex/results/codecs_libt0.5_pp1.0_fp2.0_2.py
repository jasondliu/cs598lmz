import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# set up logging
logging.basicConfig(filename='log.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)
logging.debug('Start of program')

# open and read the file
logging.debug('Opening the file')
file = open('data.txt')
lines = file.readlines()

# create the dictionary
logging.debug('Creating the dictionary')
data = {}
for line in lines:
    line = line.strip()
    logging.debug('Processing line: ' + line)
    key, value = line.split('=')
    key = key.strip()
    value = value.strip()
    data[key] = value
logging.debug('Processing completed')

# iterate through the dictionary
logging.debug('Iterating through the dictionary')
for key, value in data
