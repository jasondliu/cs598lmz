import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_text(file_path):
    with codecs.open(file_path, 'r', 'utf-8', errors='strict') as f:
        return f.read()

def get_text_from_url(url):
    response = requests.get(url)
    return response.text

def get_text_from_html(html):
    return BeautifulSoup(html, 'html.parser').get_text()

def get_words(text):
    return re.findall(r'\w+', text.lower())

def get_words_from_file(file_path):
    return get_words(get_text(file_path))

def get_words_from_url(url):
    return get_words(get_text_from_html(get_text_from_url(url)))

def get_words_from_html(html):
    return get_words(get_text_from_html(html))

def get_words_from_text(text):

