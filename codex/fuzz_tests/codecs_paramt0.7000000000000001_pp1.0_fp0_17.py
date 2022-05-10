import codecs
codecs.register_error('strict', codecs.ignore_errors)
import chardet

def convert_to_utf8(text):
    try:
        return text.encode('utf-8')
    except UnicodeEncodeError:
        return text.encode('iso-8859-1').decode('cp1252').encode('utf-8')

def get_html(url):
    try:
        html = urllib.request.urlopen(url)
    except urllib.error.HTTPError as e:
        print(e)
        return None
    except urllib.error.URLError as e:
        print(e)
        return None
    return html

def get_encoding(html):
    try:
        encoding = html.headers.get_content_charset()
    except AttributeError:
        encoding = chardet.detect(html.read())['encoding']
    return encoding

def get_soup(html):
    encoding = get_encoding(html)
    text = html.read().decode(enc
