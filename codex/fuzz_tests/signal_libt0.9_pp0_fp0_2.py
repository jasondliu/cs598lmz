import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

client = pymongo.MongoClient('mongodb://' + config.DATABASE['db_user'] + ':' + config.DATABASE['db_pass'] + config.DATABASE['db_host'])
