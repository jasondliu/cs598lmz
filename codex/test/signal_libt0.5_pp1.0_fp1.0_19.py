import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

def get_key_and_secret(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    return lines[0].strip(), lines[1].strip()

def get_token_and_secret(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    return lines[0].strip(), lines[1].strip()

def get_token(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    return lines[0].strip()

def get_secret(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    return lines[0].strip()

def get_tweets(tweets_file):
    f = open(tweets_file, 'r')
    tweets = f.readlines()

