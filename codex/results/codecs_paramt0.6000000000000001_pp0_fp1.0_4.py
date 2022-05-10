import codecs
codecs.register_error('strict', codecs.ignore_errors)

import settings

def get_tweets_by_user(username):
    try:
        user_tweets = api.GetUserTimeline(screen_name=username, count=settings.TWEETS_PER_PAGE)
    except:
        raise Exception('Twitter API error')
    return user_tweets

def get_tweets_by_hashtag(hashtag):
    try:
        user_tweets = api.GetSearch(term=hashtag, count=settings.TWEETS_PER_PAGE)
    except:
        raise Exception('Twitter API error')
    return user_tweets

def get_tweets_by_search(search):
    try:
        user_tweets = api.GetSearch(term=search, count=settings.TWEETS_PER_PAGE)
    except:
        raise Exception('Twitter API error')
    return user_tweets

def get_tweets_by_trend(trend):
    try:
        user
