import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

MATCH_COLLECTION_SLACK_ENV_VAR = 'SLACK_MATCH_COLLECTION_ENV_VAR'

FIVE_MINUTE_MS = 5 * 60 * 1000
WIN_TYPES = ['perfect', 'full', 'timed']
LOG_BATCH_SIZE = 10

class Database:
    def __init__(self, db_url, logfile_name):
        self.engine = sqlalchemy.create_engine(db_url)
        self.Session = sqlalchemy.orm.sessionmaker(bind=self.engine)
        self.db_url = db_url
        self.logfile_name = logfile_name

    def _entity_to_dict(self, entity):
        if not entity:
            return None

        return evecon.tools.entity_to_dict(entity)

    def _list_to_dict(self, lst):
        if not lst:
            return None


