import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='tweets',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


def process_status_object(status_object):
    # Process the status object to extract the relevant fields
    status_id = status_object.id_str
    created_at = status_object.created_at
    text = status_object.text
    user_id = status_object.user.id_str
    user_name = status_object.user.name
    user_screen_name = status_object.user.screen_name
    user_location = status_object.user.location
    user_followers_count = status_object.user.followers_count
    user_friends_count = status_object.user.friends_count
