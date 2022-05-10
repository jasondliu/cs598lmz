import threading
threading.stack_size(67108864)

conn = sql.connect(database="/home/pi/Documents/pi_surveillance/database/logger.db")
c = conn.cursor()

# Create table if not exists
c.execute("CREATE TABLE IF NOT EXISTS csv_data_logger(id INTEGER PRIMARY KEY AUTOINCREMENT, date_time TEXT, temperature TEXT, humidity TEXT)") # UNIX is fine for our purposes, but remember on Windows there is a DATETIME data type

# Read from csv, insert into database and then remove from filesystem
def insert_data(file_path):
    with open(file_path, 'rt') as read_obj:
        csv_reader = reader(read_obj)
        for row in csv_reader:
            c.execute("INSERT INTO csv_data_logger (date_time, temperature, humidity) VALUES (?,?,?)"
                        ,(row[0], row[1], row[2]))
            conn.commit()
            print("added to database")
    os
