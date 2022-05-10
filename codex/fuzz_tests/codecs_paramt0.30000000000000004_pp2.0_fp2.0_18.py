import codecs
codecs.register_error('ignore', codecs.ignore_errors)

def get_text_from_url(url):
    try:
        response = requests.get(url)
        response.encoding = 'utf-8'
        return response.text
    except:
        return ''

def get_text_from_file(file_name):
    try:
        with codecs.open(file_name, 'r', 'utf-8') as f:
            return f.read()
    except:
        return ''

def get_text_from_html(html):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        for script in soup(["script", "style"]):
            script.extract()
        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)
        return text
    except:
        return ''


