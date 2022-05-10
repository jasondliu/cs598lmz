import codecs
codecs.register_error('strict', codecs.ignore_errors)
#min_df: ignore words that appear in less than this fraction
#max_df: ignore words that this fraction of the documents


tf = TfidfVectorizer(lowercase=True, analyzer='word', norm='l2', stop_words="english", min_df=0.001, max_df=0.9)
tf_vectors = tf.fit_transform(pre_df['texts'])

#print(tf_vectors.shape)
#print(len(tf.get_feature_names()))
#print(tf.get_feature_names()[:10])

#print(tf_vectors.toarray())

#print(tf.vocabulary_)
#print(tf.idf_)#get idf
#print(tf_vectors)


#NMF
nmf_model = NMF(init='random', random_state=1, alpha=.1, l1_ratio=.5, n_components=5)

nmf_vectors = nmf_model.
