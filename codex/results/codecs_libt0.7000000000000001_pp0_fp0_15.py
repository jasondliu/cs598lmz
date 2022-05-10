import codecs
codecs.register(lambda name: codecs.lookup("utf-8") if name == 'cp65001' else None)
import csv

from tqdm import tqdm
from os.path import basename
from multiprocessing import Pool


from util import download_file
from util import text2int
from util import process_text


def parse_row(row):

    """
    Process a single row of the CSV
    """

    pk = row[0]
    url = row[4]
    date = row[2]
    date = date.split(" ")[0]
    date = date.replace("-", "")
    title = process_text(row[5])
    body = process_text(row[6])
    return pk + ".txt", url, date, title, body


def build_text(pk, url, date, title, body):

    """
    Build the text to be stored in the file
    """

    return "PK:{}\nURL:{}\nDATE:{}\nTITLE:{}\nBODY:{}\n".
