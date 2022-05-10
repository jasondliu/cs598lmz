import codecs
codecs.register_error('my_ignore', codecs.ignore_errors)

def tweet_similarity (tweet1, tweet2, set_size):
	
	tweets = [tweet1, tweet2]
	
	#load word embeddings
	word_embeddings = {}
	with open('wordVectors.txt', 'r') as file:
		for line in file:
			line = line.strip().split()
			inp_word = line[0]
			inp_vec = np.array(list(map(float, line[1:])))
			word_embeddings[inp_word] = inp_vec

	#calculate vector for tweet1
	max_tweet_sim_score = 0
	for tweet in tweets:
		sent_tweet_sim_score = 0
		tokens = tweet.split()
		vec_tokens = []
		for word in tokens:
			word = word.lower()
			if word in word_embeddings:

