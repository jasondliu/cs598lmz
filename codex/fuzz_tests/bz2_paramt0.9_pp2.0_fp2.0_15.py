from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(ct_bz2)

# Save ct_bz2 as ct_xml
with open('ct_xml.bz2', 'wb') as ct_bz2:  # open the file for writing
    ct_bz2.write(ct_xml)  # write the contents to the file
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

# Make an empty list: frames
frame = []
# iterate over all the elements of word_tag_pairs
for word, tag in word_tag_pairs:
    # Bind word to the unique value in the sorted list of unique words
    word = word
    # Create a list with the tag and a word
    tagged_word = (tag, word)
    # Append the tuple to the frames list
    frames.append(tagged_word)
    
print(frames)
chunks = nltk.ne_chunk(tree_tagged_words)
# POS tag each
