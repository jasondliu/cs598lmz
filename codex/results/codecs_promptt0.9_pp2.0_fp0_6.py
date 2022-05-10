import codecs
# Test codecs.register_error()
def search_function(encoding):
    if encoding == "ascii":
        return codecs.lookup("latin1")
    if encoding == "latin-1":
        return codecs.lookup("latin-1")

codecs.register_error("replace_char", codecs.replace_errors)
c='a'.encode('utf-8', 'replace')

# Sputnik 
words_set = set()
f = open(local_repo + 'corpora/bnc_words.txt', 'r')
for word in f.readlines():
    words_set.add(word.strip())
f.close()

logger.info("Loading model...")

# upload our local corpus from disk to ram, so we have fast random access
if not os.path.exists(local_repo + 'corpora/bnc.mm'):
    logger.info("loading SPUTNIK corpus...")
    local_corpus = corpora.MmCorpus(local_repo + 'corpora/bnc.mm
