import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

def test_sim_matrix_word(word,model):
	word_vectors = model.wv
	similar_words = {search_term: [item[0] for item in word_vectors.most_similar([search_term], topn=5)]
                  for search_term in [word]}
	return similar_words

def test_sim_matrix_vec(vec,model):
	similar_words = {search_term: [item[0] for item in model.most_similar([search_term], topn=5)]
                  for search_term in [vec]}
	return similar_words

def test_vec_matrix_word(word,model):
	word_vectors = model.wv
	return word_vectors[word]

def test_vec_matrix_vec(vec,model):
	return model[vec]

def test_load_vec_matrix(arch):
	model = KeyedVect
