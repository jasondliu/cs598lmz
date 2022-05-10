import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

def load_dicts(path):
    print('loading')
    with open(path, 'rb') as f:
        d = pickle.load(f)
    return d

def save_dicts(d, path):
    print('saving')
    with open(path, 'wb') as f:
        pickle.dump(d, f)

def clean_text(text):
    text = text.lower()
    text = text.replace('\n', ' ')
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text

def get_text(url):
    html = urlopen(url).read()
    bsObj = BeautifulSoup(html, 'html.parser')
    text = bsObj.find('div', {'id': 'mw-content-text'}).get_text()
    return text

def get
