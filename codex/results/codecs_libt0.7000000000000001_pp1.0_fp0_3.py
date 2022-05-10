import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

def get_cursor():
    return MySQLdb.connect(host="localhost",user="root",passwd="root",db="db_weibo",charset="utf8").cursor()

def get_all_cursor():
    cur = MySQLdb.connect(host="localhost",user="root",passwd="root",db="db_weibo").cursor()
    cur.execute("select user_id from t_user_tb")

    users = []
    for row in cur.fetchall():
        users.append(row[0])

    return users

def insert_user(user_id, screen_name, location, description, profile_image_url, gender, followers_count, friends_count, verified, verified_type, statuses_count):
    cursor = get_cursor()
    try:
        cursor.execute("insert into t_user_tb(user_id, screen_name, location, description, profile_image_url,
