import codecs
codecs.register_error('strict', codecs.strict_errors)

# load data
print('Loading data...')
data = json.load(open(FLAGS.data_dir + 'data.json', encoding='utf-8'))
train_data = data['train']
test_data = data['test']

# load glove
print('Loading Glove...')
vocab = defaultdict(float)
dim = 0

# build glove
with open(FLAGS.glove_path, 'r', encoding='utf-8') as fh:
    for line in fh:
        array = line.split()
        word = array[0]
        vector = list(map(float, array[1:]))
        dim = len(vector)
        vocab[word] = vector

# process train data
print('Processing training data...')
train_questions = []
train_question_masks = []
train_question_lengths = []
train_passages = []
train_passage_masks = []
train_passage_lengths = []
train_labels = []
