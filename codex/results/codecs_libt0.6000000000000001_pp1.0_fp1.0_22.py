import codecs
codecs.open('predict.txt', 'w', 'utf-8')
# test
test_data_path = './test/test.txt'
test_data = open(test_data_path, 'r', encoding='utf-8')

test_labels = []
test_questions = []
test_answers = []

for line in test_data:
    line = line.strip().split('\t')
    test_labels.append(int(line[0]))
    test_questions.append(line[1])
    test_answers.append(line[2])

test_questions_pad = pad_sequences(tokenizer.texts_to_sequences(test_questions), maxlen=MAX_SEQUENCE_LENGTH)
test_answers_pad = pad_sequences(tokenizer.texts_to_sequences(test_answers), maxlen=MAX_SEQUENCE_LENGTH)

# test
test_questions_pad = np.array(test_questions_pad)
test_
