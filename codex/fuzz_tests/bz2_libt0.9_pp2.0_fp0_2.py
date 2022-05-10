import bz2
bz2read = lambda fname: bz2.BZ2File(fname).read().decode('utf-8')

# Generate the single-document search index
indexdir = environ.get('ECCOTEXT_INDEX', 
    #% dirs['unicode'].by_fn['utf8/17']
    '/home/selth/code/ecco_text/eccotext_raw_to_split/unicode/utf8/17')

# read solr index source configuration
#% solrconfig-template = dirs['unicode'].by_fn['solrconfig-template.xml']
solrconfig_template = '/home/selth/code/ecco_text/eccotext_raw_to_split/unicode/solrconfig-template.xml'
with open(solrconfig_template) as sctf:
    solrconfig_str = sctf.read()

# modify index directory
solrconfig = solrconfig_str.format(indexdir=indexdir)
# make solrconfig readable/writable
