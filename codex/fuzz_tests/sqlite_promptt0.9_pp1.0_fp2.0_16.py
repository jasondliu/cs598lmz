import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() capability:
from test_sqlite_capability import test_sqlite_capability


# Define sqlite3.connect() capabilities to be tested:
connect_capability = {
    'Synchronous' : { 
        'off' : 'OFF',
        'full' : 'FULL',
        'normal' : 'NORMAL'},
    'Locking' : { 
        'exclusive' : 'EXCLUSIVE',
        'normal' : 'NORMAL'}
}

class t_sqlcipher_key_generation():

    """
    Encapsulates all tests for verifying sqlcipher updates when encrypting a database.
    """

    def __init__(self, nuzlocke, diagnostic_database_file, seed_random_generator=True,
        master_password_key='12345678901234567890123456789012', 
        encrypted_database_file='enc_t_sqlcipher_key_generation.db'):

        self.nuzlocke = nuzlocke
        self.diagnostic_database_file = diagnostic
