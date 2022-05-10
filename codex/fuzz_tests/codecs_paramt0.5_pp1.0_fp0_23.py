import codecs
codecs.register_error('replace_with_space', lambda e: (u' ', e.start + 1))

# with codecs.open("data/ptb.train.txt", "r", "utf-8", "replace_with_space") as f:
#     text = f.read()

# #print text
# print len(text)

# print text[:1000]

# # Tokenize the text.
# tokenizer = Tokenizer(lower=True, filters='')
# tokenizer.fit_on_texts([text])

# print tokenizer.word_index

# # Tokenize the text.
# tokenizer = Tokenizer(num_words=None, lower=True, split=" ")
# tokenizer.fit_on_texts([text])

# print tokenizer.word_index

# print tokenizer.texts_to_sequences(["I am a test"])

# # Tokenize the text.
# tokenizer = Tokenizer(num_words=None, char_level=True, lower=True)
# tokenizer.fit_on_text
