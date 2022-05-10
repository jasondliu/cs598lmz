import lzma
lzma.decompress(b1)

# Reading lzma file and writing a csv file
import lzma, gzip, csv
# z = lzma.open('/content/drive/My Drive/Twitter Sentiment Analysis Project/Twitter-Sentiment-Analysis/kaggle-dataset/training.1600000.processed.noemoticon.csv.lzma', 'r')
f = gzip.open('/content/drive/My Drive/Twitter Sentiment Analysis Project/Twitter-Sentiment-Analysis/kaggle-dataset/processing.txt.gz', 'wb')

with open('/content/drive/My Drive/Twitter Sentiment Analysis Project/Twitter-Sentiment-Analysis/kaggle-dataset/training.1600000.processed.noemoticon.csv.lzma', 'r') as z:
  count = 2200000
  while count <= 2700000:
    with open ('/content/drive/My Drive/Twitter Sentiment Analysis Project/Twitter-Sentiment-Analysis/kaggle-dataset/processing.txt', 'a')
