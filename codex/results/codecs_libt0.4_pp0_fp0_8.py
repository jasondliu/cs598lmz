import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

#Get the data
df = pd.read_csv('data_final.csv')

#Create a new dataframe with only the columns we want
df_small = df[['id','text','retweet_count','favorite_count','lang','user_id','user_name','user_screen_name','user_followers_count','user_friends_count','user_favourites_count','user_statuses_count','user_location','user_created_at','user_verified','user_description','user_default_profile','user_default_profile_image','user_has_extended_profile','user_profile_use_background_image','user_profile_background_image_url','user_profile_image_url','user_profile_banner_url','user_profile_background_color','user_profile_text_color','user_profile_link_color','user_profile_sidebar_border_color','user_profile_sidebar_fill_color','user_profile
