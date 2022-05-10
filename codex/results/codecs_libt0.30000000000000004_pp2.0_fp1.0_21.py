import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# Connect to MySQL
conn = pymysql.connect(host='localhost', user='root', password='', db='mydb', charset='utf8mb4')
c = conn.cursor()

# Create a new table
c.execute("""CREATE TABLE IF NOT EXISTS tweets (
            id int(11) NOT NULL AUTO_INCREMENT,
            user_id varchar(255) NOT NULL,
            user_name varchar(255) NOT NULL,
            user_screen_name varchar(255) NOT NULL,
            user_location varchar(255) NOT NULL,
            user_followers_count int(11) NOT NULL,
            user_friends_count int(11) NOT NULL,
            user_created_at varchar(255) NOT NULL,
            user_time_zone varchar(255) NOT NULL,
            user_profile_background_color varchar(255) NOT NULL,
            user_
