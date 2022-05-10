import codecs
codecs.register_error('strict', codecs.ignore_errors)

#%%
# Initialize the model
model = KeyedVectors.load_word2vec_format('../../data/word2vec/GoogleNews-vectors-negative300.bin', binary=True)

#%%
# Function to convert a sentence to a vector
def sentence_vector(sentence, model):
    v = np.zeros(300)
    count = 0
    for w in sentence.split():
        try:
            v += model[w]
            count += 1
        except KeyError:
            pass
    v = v / count
    return v

#%%
# Create a list of vectors for each sentence
sentence_vectors = []
for sentence in sentences:
    v = sentence_vector(sentence, model)
    sentence_vectors.append(v)

#%%
# Create a dataframe with the vectors
sentence_vectors_df = pd.DataFrame(sentence_vectors)
sentence_vectors_df.head()

#%%
# Create a dataframe with
