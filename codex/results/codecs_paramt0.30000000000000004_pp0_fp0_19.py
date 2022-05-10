import codecs
codecs.register_error('strict', codecs.ignore_errors)

# We use a custom tokenizer that is more permissive than the default one.
# This is necessary to handle some of the weird spacing in the text.
# We also skip over all the lines that contain the string "Chapter"
# because these are chapter headings.
def custom_tokenizer(text):
    return [token for token in text.split() if token != 'Chapter']

# We also need a custom sentence splitter that is more permissive than the default one.
# This is necessary to handle some of the weird spacing in the text.
# We also skip over all the lines that contain the string "Chapter"
# because these are chapter headings.
def custom_sentence_splitter(text):
    return [sentence for sentence in text.splitlines() if sentence != 'Chapter']

# We also need a custom paragraph splitter that is more permissive than the default one.
# This is necessary to handle some of the weird spacing in the text.
# We also skip over all the lines that contain the string "Chapter"
# because these are chapter headings.
def
