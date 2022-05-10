import select

import pytest

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

from mongorm import Database
from mongorm.connection import Connection
from mongorm.document import Document


@pytest.fixture(scope='function')
def mongo_client():
    client = MongoClient(serverSelectionTimeoutMS=1)
    try:
        client.admin.command('ismaster')
    except ConnectionFailure:
        pytest.skip('No MongoDB server running')
    return client


@pytest.fixture(scope='function')
def mongo_db(mongo_client):
    return mongo_client.test


@pytest.fixture(scope='function')
def mongo_connection(mongo_db):
    return Connection(db=mongo_db)


@pytest.fixture(scope='function')
def mongo_database(mongo_connection):
    return Database(connection=mongo_connection)


