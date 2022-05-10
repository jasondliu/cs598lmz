import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

def get_data(filename):
    with codecs.open(filename, 'r', 'utf-8', 'replace_with_space') as f:
        data = f.read()
        data = data.split('\n')
        data = [x.split('\t') for x in data if len(x)>=1]
        [english_sentence, french_sentence] = [list(x) for x in zip(*data)]
        english_sentence = [s.split(' ') for s in english_sentence]
        french_sentence = [s.split(' ') for s in french_sentence]
        return english_sentence, french_sentence

english_sentences, french_sentences = get_data('small_vocab_en')
print('Dataset Loaded')

for sample_i in range(2):
    print('small_vocab_en Line {}:  {}'.format(sample_i + 1, english_sentences[sample_i]))

