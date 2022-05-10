from bz2 import BZ2Decompressor
BZ2Decompressor

# Code for reading data from wiki dumps (inspired by: https://github.com/panyang/Wikipedia_Word2vec/blob/master/v1/process_wiki.py)

def process_wiki(read_file, write_file, test = False):
    output = open(write_file, 'w', encoding='utf-8')
    articles, articles_all = 0, 0
    space = " "
    i = 0
    if test:
        wiki = bz2.BZ2File(read_file)  # bz2 file
    else:
        wiki = open(read_file, 'r', encoding="utf-8")  # plain text file
    
    skip = False
    refs = False
    article_text = ""
    skipped_count = 0
    for line in wiki:
        if "<page>" in line:
            skip = False
            refs = False
        elif test and '<title>' in line and ('List' in line or 'Wikipedia' in line or 'Category' in line or pieces[0] in line):
            skip
