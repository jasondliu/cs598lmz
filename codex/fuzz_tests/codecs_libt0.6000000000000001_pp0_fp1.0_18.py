import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)
import sys
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

def get_hot_topics(n_topics, n_words):
    # get the top n_topics topics
    with open(os.path.join(path_to_topics, "topics.csv"), "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        headers = next(reader)
        topics = []
        for row in reader:
            topics.append(row)

    # get the top n_words words for each topic
    with open(os.path.join(path_to_topics, "topic-word-distribution.csv"), "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        headers = next(reader)
        words = []
        for row in reader:
            words.append(row)
        words.
