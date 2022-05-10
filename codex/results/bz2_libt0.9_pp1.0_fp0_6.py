import bz2
bz2file = os.path.abspath('../data/enwiki-latest-pages-articles.xml.bz2')
bz2.decompress(bz2file)

with bz2.open('enwiki-latest-pages-articles', 'rb') as i:
    with open('enwiki-latest-pages-articles.822M.txt', 'wb') as o:
        for d in i:
            o.write(d)
def gen_xml_sents(fname):
    with open(fname) as f:
        for l in f:
            yield l
        
def sent_generator(fname):
    for sent in gen_xml_sents(fname):
        if sent.startswith('<doc'):
            cur_doc_lines = []
        elif sent.startswith('</doc>'):
            yield cleanup(' '.join(cur_doc_lines))
        else:
            cur_doc_lines.append(sent.strip())

def cleanup(text):
    # strip wiki tags
    text = re
