import bz2
bz2file = bz2.BZ2File('reuters21578.json')
contents = bz2file.read()

data = json.loads(contents, encoding='utf-8')
print(type(data))

data = data[:1000]


## Load Data into pandas DataFrame

import pandas as pd
news_articles = pd.DataFrame(data)
news_articles.head(5)


print(len(news_articles))


## Clean Data

print(news_articles['topic'].value_counts())

news_articles = news_articles[news_articles['topic'].isin(['acq', 'earn', 'crude', 'trade'])]
print(len(news_articles))

print(news_articles['topic'].value_counts())


## Write Data to CSV file

news_articles.to_csv('news_articles.csv')
