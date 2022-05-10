import codecs
codecs.register(lambda name: name == 'cp65001' and codecs.lookup('utf-8') or None)

# import locale
# locale.setlocale(locale.LC_ALL, '')

def main():
    # First, we'll create an instance of the API class.
    api = twitter.Api(consumer_key='',
                      consumer_secret='',
                      access_token_key='',
                      access_token_secret='')

    # Show the user's name.
    # print(api.VerifyCredentials().name)
    # print(api.GetUser(user_id=None, screen_name=None, include_entities=None))

    # Get the last 20 tweets from the public timeline.
    # print(api.GetPublicTimeline())

    # Get the last 20 tweets from the home timeline.
    # print(api.GetHomeTimeline())

    # Get the last 20 tweets from the user's timeline.
    # print(api.GetUserTimeline())

    # Get the tweets from a user's timeline.
    # print(
