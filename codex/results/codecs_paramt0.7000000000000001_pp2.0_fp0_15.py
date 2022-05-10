import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------

class User:
    def __init__(self, id, name, screen_name, location, description, url,
                 followers_count, friends_count, listed_count, favourites_count,
                 statuses_count, created_at, time_zone, lang, profile_image_url,
                 protected, geo_enabled, time_zone_offset, utc_offset,
                 verified, followers_ratio, friends_ratio, klout_score,
                 sentiment_score, sentiment_magnitude, gender, race, age_range,
                 age_inferred):
        self.id = id
        self.name = name
        self.screen_name = screen_name
        self.location = location
        self.description = description
        self.url = url
        self.followers_count = followers_count
        self.friends_count = friends_count
        self.listed_count = listed_count
        self.favourites_count = favourites_count
        self.statuses_count = statuses_
