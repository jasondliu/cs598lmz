import codecs
codecs.register_error('replace_with_space', lambda e: (u' ',e.start + 1))

#load the data
tweets = pd.read_csv('../data/processed/tweets.csv', encoding='utf-8', error_bad_lines=False, warn_bad_lines=False)

#load the dictionary
with codecs.open('../data/processed/dictionary.txt', 'rb', encoding='utf-8', errors='replace_with_space') as f:
    dictionary = f.read().splitlines()

#create a word cloud
text = " ".join(word for word in dictionary)
wordcloud = WordCloud(width=1600, height=800, max_font_size=200).generate(text)
plt.figure(figsize=(12,10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

#create a word cloud for the tweets
text = " ".join(word for word in tweets['text'])
wordcloud = WordCloud(width=1600,
