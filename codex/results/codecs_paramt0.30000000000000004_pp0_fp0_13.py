import codecs
codecs.register_error('strict', codecs.ignore_errors)

#
# The following functions are used to build the database
#

#
# This function is used to build the database from the raw data
#
def build_db(db_name, db_path, raw_path):
    #
    # Open the database
    #
    conn = sqlite3.connect(db_path + db_name)
    c = conn.cursor()

    #
    # Create the tables
    #
    c.execute('''CREATE TABLE IF NOT EXISTS raw_data (
    id INTEGER PRIMARY KEY,
    date TEXT,
    time TEXT,
    time_zone TEXT,
    latitude REAL,
    longitude REAL,
    depth REAL,
    magnitude REAL,
    mag_type TEXT,
    nb_stations INTEGER,
    gap REAL,
    distance REAL,
    rms REAL,
    source TEXT,
    event_id TEXT,
    version TEXT,
    updated TEXT,
    place TEXT,
    type TEXT)''')
    c.
