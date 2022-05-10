import bz2
bz2.decompress(bz2.compress(
    pickle.dumps(prepared_vectors_matrix))).encode('utf8')
md.visualize_prepared_vectors(
    prepared_vectors_matrix, model.wv.vocab)
 
 
model = doc2vecize(sentences,
                   OUTPUT_FILE_NAME,
                   vector_size=100,
                   min_count=1,
                   window=4,
                   sg=1,
                   use_tfidf=True,
                   workers=8,
                   epochs=15)
model = load_d2v_model(OUTPUT_FILE_NAME)
prepared_vectors_matrix = md.prepare_vectors_matrix(vectors_matrix)
md.visualize_prepared_vectors(prepared_vectors_matrix, model.wv.vocab)
prepared_vectors_matrix
prepared_vectors_matrix['церковь']['saint_pude']
pre
