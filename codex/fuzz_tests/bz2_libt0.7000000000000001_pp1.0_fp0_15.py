import bz2
bz2.BZ2File('raw_sentences.txt.bz2', 'r')

# Get a list of all of the file names, then loop through that list.
# This is where I loop through all of the file names, calling the 
# above function for each one, and appending the results to the 
# list of dictionaries.

file_list = glob.glob('/home/jf/Desktop/Data-Science-Exercises/Movie_Reviews/txt_sentoken/pos/*.txt')
pos_dict = []

for i in file_list:
    pos_dict.append(tokenizer(i))

# Do the same for the negative reviews

file_list2 = glob.glob('/home/jf/Desktop/Data-Science-Exercises/Movie_Reviews/txt_sentoken/neg/*.txt')
neg_dict = []

for i in file_list2:
    neg_dict.append(tokenizer(i))
    
# At this point I have two lists of dictionaries, one for positive reviews,
# one for
