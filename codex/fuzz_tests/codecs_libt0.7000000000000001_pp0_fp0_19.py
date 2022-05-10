import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# open the connection to MySQL
db = MySQLdb.connect(host=config_dict['db_host'],
                     user=config_dict['db_user'],
                     passwd=config_dict['db_pass'],
                     db=config_dict['db_name'],
                     use_unicode=True,
                     charset="utf8mb4")

# This creates the cursor, which allows us to execute MySQL commands within Python.
cursor = db.cursor()

try:
    # Drop the table if it already exists
    cursor.execute("DROP TABLE IF EXISTS btc_transactions")

    # Create the table
    cursor.execute("CREATE TABLE btc_transactions (" +
                   "timestamp DATETIME, " +
                   "txid CHAR(64), " +
                   "source CHAR(34), " +
                   "destination CHAR(34), " +
                   "amount DECIMAL(16,8), " +
                  
