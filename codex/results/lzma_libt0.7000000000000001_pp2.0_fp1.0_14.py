import lzma
lzma_decomp = lzma.LZMADecompressor()

# load data
with open('data_20200422/dblp_papers_v11_data_10GB.txt.xz', 'rb') as f:
    data = lzma_decomp.decompress(f.read()).decode('utf-8')

# strip header and footer
data = data.split('\n\n')[1][:-1]

# get list of papers
papers = data.split('\n\n')

# get list of authors
all_authors = [paper.split('\n')[2] for paper in papers]
# remove non-author fields
authors = []
for a in all_authors:
    authors.extend(a.split('; ')[:-1])
# remove whitespace
authors = [a.strip() for a in authors]
# remove duplicates
authors = list(set(authors))
# sort
authors.sort()

# format authors
authors_formatted = []
for a in authors:
    if len
