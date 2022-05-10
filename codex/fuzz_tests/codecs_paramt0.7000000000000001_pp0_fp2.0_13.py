import codecs
codecs.register_error("strict", codecs.ignore_errors)

# Read input file, assume it is UTF-8 encoded
with codecs.open("dateien/corpus.txt", "r", "utf-8") as f:
    text = f.read()

# create a word cloud
wordcloud = WordCloud(
    width=1800,
    height=1400,
    max_words=200,
    background_color="white",
    stopwords=stopwords_german,
    contour_width=1,
    contour_color="steelblue"
).generate(text)

# Save word cloud as an image
wordcloud.to_file("dateien/wordcloud.png")
