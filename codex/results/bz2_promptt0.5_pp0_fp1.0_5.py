import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
with gzip.open('data/enwiki-latest-pages-articles.xml.bz2', 'rb') as infile:
    with open('data/enwiki-latest-pages-articles.xml', 'wb') as outfile:
        outfile.write(decompressor.decompress(infile.read()))

# Extracting the data

# In[3]:


def extract_pages(input_file):
    """
    Extract pages from the bz2 file
    """
    with bz2.open(input_file, 'rb') as infile:
        page = []
        for line in infile:
            line = line.decode('utf-8')
            if line.startswith('    <page>'):
                page = []
            page.append(line)
            if line.startswith('    </page>'):
                yield ''.join(page)

def extract_text(page):
    """
    Extract the text from an article
    """

