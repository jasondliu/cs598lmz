import codecs
codecs.register_error("ignore", codecs.replace_errors) #.encode( 'utf-8', errors='ignore' )

# compile the tokenizer
re_tok = re.compile('([{}“”¨«»®´·º½¾¿¡ß±≠≤≥∞¶·∑∏π¬√⁄€‹›ﬁﬂ»“”¨«†ஃப்புபன்])')

def tokenize(s): return re_tok.sub(r' \1 ', s.lower()).split()

n = train["comment_text"].shape[0]
vec = TfidfVectorizer(ngram_range=(1,2), tokenizer=tokenize,
               min_df=3, max_df=0.9, strip_accents='unicode', use_idf=1,
               smooth_idf=1, sublinear_tf=1 )
trn_term_doc = vec
