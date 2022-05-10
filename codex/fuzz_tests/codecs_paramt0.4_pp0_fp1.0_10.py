import codecs
codecs.register_error('replace_spaces', lambda e: (u'\uFFFD', e.start + 1))

class Tweet(object):
    def __init__(self, tweet_id, text, time, user_id, user_name, user_screen_name, user_followers_count, user_friends_count, user_location, user_lang, user_time_zone, user_statuses_count, user_created_at, user_verified, user_description, user_url, user_listed_count, user_favourites_count, user_geo_enabled, user_profile_image_url, user_default_profile_image, user_utc_offset, user_time_zone, user_profile_background_color, user_profile_image_url_https, user_profile_background_image_url, user_profile_background_image_url_https, user_profile_background_tile, user_profile_link_color, user_profile_sidebar_border_color, user_profile_sidebar_fill_color, user_profile_text_color, user_profile_use_background
