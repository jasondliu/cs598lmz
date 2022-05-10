import threading
threading.stack_size(2**27)

class StdOutListener(tweepy.StreamListener):

    def on_data(self, data):
        try:
            data_clean = data.replace(' b\'', '')
            data_clean = data.replace('\\n', '')
            data_clean = data.replace('\\', '')
            jdat = json.loads(data_clean)
            print('------------------')
            #print(jdat['text'])
            for hashtag in jdat['entities']['hashtags']:
                print(hashtag['text'])

        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(
