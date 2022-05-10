import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space) 

def get_stop_words(file_path):
    with open(file_path, 'r', encoding="utf-8") as f:
        stop_words = f.read().splitlines()
    return stop_words

def get_all_tweets_from_file(file_path):
    with open(file_path, 'r', encoding="utf-8", errors='replace_with_space') as f:
        tweets = f.read().splitlines()
    return tweets

def get_all_tweets_from_files(files_path):
    all_tweets = []
    for file_path in files_path:
        all_tweets.extend(get_all_tweets_from_file(file_path))
    return all_tweets

def get_all_tweets_from_csv(csv_path):
    all_tweets = []
    with open(csv_path, 'r', encoding="utf-8") as f:
