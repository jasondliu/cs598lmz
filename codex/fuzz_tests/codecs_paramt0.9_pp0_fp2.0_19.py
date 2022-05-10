import codecs
codecs.register_error('strict', codecs.ignore_errors)
## https://stackoverflow.com/questions/29462434/reading-text-from-pdf-with-pypdf-unexpected-end-of-data-error
from pprint import pprint
from argparse import Namespace

from glob import glob
# manually sort in numerical order
# bib_list = glob('annual-bib-files/*.bib')

# open file, first line is filename, remaining lines are bibtex
with open('annual-bib-files/bib_list.txt','r') as fin:
    bib_list = [ line.strip() for line in fin.readlines()]
bib_files = bib_list[1:] # bib_list[0] is the list index
# bib_files = glob('annual-bib-files/*.bib')

# https://stackoverflow.com/questions/22806270/iterating-through-a-list-of-values-bibtexparser

def bib_item_to_annual
