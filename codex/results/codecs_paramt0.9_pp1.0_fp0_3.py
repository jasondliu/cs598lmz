import codecs
codecs.register_error('replace_pswd', codecs.lookup_error('replace_password'))

from . import db, file_repo, cache, config as app_config

from .common import log, log_data
from .decorators import with_db_session
from .account_repo import AccountRepo

from . import storage_providers


class Service(object):
    def __init__(self, config=None):
        self.db = db
        self.config = config
        self.cache = cache.Cache()
        self.file_repo = file_repo.FileRepo(config)
        self.storage_providers = storage_providers.StorageProviders(self.config)
        db.init(self.config)
        self.file_repo.init()
        self.account_repo = AccountRepo(self.config, self.db)

    def from_storages_ids(self, ids):
        """identify file storages from given IDs

        args:
            ids (list): list of IDs of file storage we need
