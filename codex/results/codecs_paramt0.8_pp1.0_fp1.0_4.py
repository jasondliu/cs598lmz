import codecs
codecs.register_error('ignore', codecs.ignore_errors)
codecs.getencoder('latin-1')

# path to EWC_models/
EWC_path = 'EWC_models/'
if not os.path.exists(EWC_path):
    os.makedirs(EWC_path)
# path to tensorboard logs
log_path = 'EWC_logs/'
if not os.path.exists(log_path):
    os.makedirs(log_path)
# path to our default text files
data_path = './data/'
if not os.path.exists(data_path):
    os.makedirs(data_path)

# load text
text = open(data_path + 'input.txt', 'r', encoding='latin-1')
text = text.read()
# convert text to lowercase
text = text.lower()
# map unique chars to ints
chars = sorted(list(set(text)))
char_to_int = dict((c, i) for i, c in enumerate
