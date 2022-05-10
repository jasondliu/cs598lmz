import mmap
# Test mmap.mmap()
# Procedure: 
#    1. Open file and map it
#    2. Read first line as an integer: number of lines in file
#    3. For all lines, read them, parse them and store in a list
#        3.1 Store each value in an index in the list 
#        3.2 Each value is separated by a space (it is a Word embedding file, use read() instead of readline for size reasons)
#        3.3 The word is stored in words[i][0]
#    4. Get the embedding and word of query from the user
#    5. Call functions within the list as follows:
#         results[0] = find_similar_words_by_vector(words, query_embedding, 10)
#         results[1] = find_similar_words_by_word(words, query_word, 10)
#         results[2] = find_similar_words_by_vector_threshold(words, query_embedding, 0.7)
#         results[3] = find_similar_words_by_word_threshold(words,
