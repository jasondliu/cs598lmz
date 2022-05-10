import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

from feed_maker_util import Config
from feed_maker_util import Log
from feed_maker_util import HayatoParseUrl
from feed_maker_util import HayatoFeedMaker

def main():
    config = Config()
    config.read_config()
    conn = MySQLdb.connect(host=config.db_host, user=config.db_user, passwd=config.db_passwd, charset="utf8mb4")
    cursor = conn.cursor()
    cursor.execute("USE " + config.db_name)

    default_log = Log(config.log_dir + "/default.log")
    feed_log = Log(config.log_dir + "/feed.log")
    cursor.execute("SELECT url FROM " + config.db_name + ".crawl_list WHERE site='hayato'")
    urls = cursor.fetchall()
    for (url,) in urls:
        if url is not None:

