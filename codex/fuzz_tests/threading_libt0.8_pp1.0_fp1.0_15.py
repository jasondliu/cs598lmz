import threading
threading.currentThread().name = 'main'
# Configure logging
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# Set values for various parameters
num_features = 300    # Word vector dimensionality
min_word_count = 40   # Minimum word count
num_workers = 16       # Number of threads to run in parallel
context = 10          # Context window size
downsampling = 1e-3   # Downsample setting for frequent words

# Initialize and train the model
model = gensim.models.word2vec.Word2Vec(sg=0, size=num_features, min_count=min_word_count, workers=num_workers, window=context, sample=downsampling)
model.build_vocab(train_arrays)
model.train(train_arrays, total_examples=model.corpus_count, epochs=model.iter)

# If you don't plan to train the model any further, calling
# init_s
