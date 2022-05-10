import codecs
codecs.open('../data/tweets_list.p', 'wb', encoding='utf-8')

import pickle
pickle.dump(tweets_list, open('../data/tweets_list.p', 'wb'))
tweets_list = pickle.load(open('../data/tweets_list.p', 'rb'))
tweets_list[0]

# %%
import pandas as pd
tweets_df = pd.DataFrame(tweets_list)
tweets_df.head(2)

# %%
# get user name and screen name
tweets_df['user_name'] = tweets_df['user'].apply(lambda x: x['name'])
tweets_df['user_screen_name'] = tweets_df['user'].apply(lambda x: x['screen_name'])
tweets_df['user_id'] = tweets_df['user'].apply(lambda x: x['id'])
tweets_df['user_verified'] = tweets_df['
