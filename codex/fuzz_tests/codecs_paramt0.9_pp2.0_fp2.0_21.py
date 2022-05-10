import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)
corpora = {}
for file in filelist:
    with codecs.open(file, encoding='utf-8', errors='replace_with_space') as temp_file:
        raw = [line.strip().split() for line in temp_file]
    raw_filt = [sent for sent in raw if len(sent) != 0]
    print file, len(raw_filt)
    corpora[file] = raw_filt
with codecs.open(file, encoding='utf-8', errors='replace_with_space') as temp_file:
    raw = [line.strip().split() for line in temp_file]
    raw_filt = [sent for sent in raw if len(sent) != 0]
 
print file, len(raw_filt)

# load stopwords
with codecs.open('stopwords.txt', encoding='utf-8') as f:
    stopwords = [line.strip() for line in f]
    stopwords = set(stopwords)

neg_
