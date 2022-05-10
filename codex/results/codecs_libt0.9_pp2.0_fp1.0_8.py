import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# CLIENT SECRETのパスを取得
API_User = '' # クライアントIDを入力
API_SECRET = '' # クライアントシークレットを入力
USER_AGENT = 'Getting Tweets for hashtag push'

# アクセストークンを利用してTwitter APIにアクセス
auth = tweepy.OAuthHandler(API_User, API_SECRET)
api = tweepy.API(auth)

# 検索関数
def get_tweets(q, count = 10):
    ''' Parameter: q = search query string, count = number of tweets to search '''
    
    # 全ツイートを格納するリスト
    tweets = []
    
    try:
        # クエリをTwitter APIに送信
        fetched
