import codecs
codecs.register_error('strict', codecs.ignore_errors)

# == DEFINE THE PATH TO YOUR MODEL & CORPUS ==

# The model needs to be a directory
# The corpus needs to be a columnar file with one token per line
model_path = "/mnt/c/Users/ealex/Desktop/Dissertation/models/20180313_0430_50_d300_alldata/"
model_path_encoded = model_path.replace(" ", "%20") # a single bug in urllib2 won't let me use spaces in path names
corpus_path = "/mnt/c/Users/ealex/Desktop/Dissertation/Corpus/corpus_filtered_lemma.txt"

# == DEFINE THE PARAMETERS OF THE MODEL ==
# Parameters:
#	- max_vocab_size: how many distinct tokens are allowed in the vocabulary
#	- num_topics: how many topics to calculate
#	- num_iterations: how many iterations of Gibbs sampling to perform
max_vocab_size = 100000
num_top
