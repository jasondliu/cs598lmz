import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

def parse_data(filename):
    df = pd.read_csv(filename, encoding='utf-8', engine='python', error_bad_lines=False, warn_bad_lines=True)
    df['text'] = df['text'].str.replace('[^\w\s]', ' ')
    df['text'] = df['text'].str.replace('[\d]', ' ')
    df['text'] = df['text'].str.replace('\s+', ' ')
    df['text'] = df['text'].str.replace('\\s+', ' ')
    df['text'] = df['text'].str.replace('\n', ' ')
    df['text'] = df['text'].str.replace('\\n', ' ')
    df['text'] = df['text'].str.replace('\t', ' ')
    df['text'] = df['text'].str.replace('\\t', ' ')
    df['text'] =
