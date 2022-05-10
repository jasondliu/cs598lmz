import codecs
codecs.register_error('strict', codecs.ignore_errors)

def readfile(filename):
    with codecs.open(filename, 'r', 'utf-8') as f:
        text = f.read()
    text = text.replace('\x00', '').replace('\x1e', '').replace('\x1f', '')
    return text

def get_sentences(text):
    sentences = (line.strip() for line in text.splitlines() if line)
    sentences = list(sentence for sentence in sentences if sentence)
    return sentences

def get_text_and_dates(sentences):
    text, dates = '', []
    for sentence in sentences:
        if re.match(r'\d{4}-\d{2}-\d{2}', sentence):
            dates.append(sentence)
        else:
            text += sentence
    return text, dates

def get_paragraphs(text):
    paragraphs = re.split(r'\n{2,}', text)
    paragraphs = list(p.strip() for
