import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

import nltk

def process(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9]', ' ', text)
    return ' '.join(text.split())
    
    
def read_data(file_name, file_name_output, limit=None):
    data = []
    with codecs.open(file_name, 'r', 'utf-8', 'replace_with_space') as f:
        for i, line in enumerate(f):
            if limit and i == limit:
                break
            if i % 10000 == 0:
                print('[{}]\tProcessing line {}'.format(datetime.now(), i))
            data += [(process(line), 1)]
        f.close()
        
    with codecs.open(file_name_output, 'w', 'utf-8', 'replace_with_space') as f:
        for line in data:
            f.write('{
