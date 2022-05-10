import lzma
lzma.LZMAFile
from textCleaning import clean
from ria import ria_parser
import pickle

session = None


def get_session():
    global session
    if not session:
        session = requests.session()
        session.headers.update({
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"})
    return session


def get_text(url):
    r = get_session().get(url)
    return r.text


asp_list = asp_parser.get_pages()
stock_list = stock_parser.get_pages()
ria_list = ria_parser.get_pages()


def get_page(url):
    print('get page: ', url)
    tm = time.time()
    t = get_text(url)
    print('page downloaded:', time.time() - tm)
    t
