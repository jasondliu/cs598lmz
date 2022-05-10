import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

# Regex for tokenizing
token_pattern = r"(?u)\b\w\w+\b"

# Set values for various parameters
feature_size = 5000    # Word vector dimensionality  
context = 10          # Context window size                                                                                    
downsampling = 1e-3   # Downsample setting for frequent words

# Initialize and train the model (this will take some time)
print("Training Word2Vec model...")
model = word2vec.Word2Vec(sentences, workers=num_workers, \
            size=feature_size, min_count = min_word_count, \
            window = context, sample = downsampling)

# If you don't plan to train the model any further, calling 
# init_sims will make the model much more memory-efficient.
model.init_sims(replace=True)

# It can be helpful to create a meaningful model name and 
# save the model for later use. You can load it later using Word2Vec.load
