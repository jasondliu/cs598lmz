import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

def get_last_update_date(db_con):
    cursor = db_con.cursor()
    cursor.execute("select max(updated_datetime) from google_play_apps
