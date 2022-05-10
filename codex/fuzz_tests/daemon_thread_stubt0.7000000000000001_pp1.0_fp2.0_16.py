import sys, threading

def run():
    db_file = 'db/snakes.db'
    db_is_new = not os.path.exists(db_file)

    with sqlite3.connect(db_file) as conn:
        if db_is_new:
            print('Creating schema')
            schema = open('db/schema.sql').read()
            conn.executescript(schema)
        else:
            print('Database exists, assume schema does, too.')

        print('Creating test data')
        conn.execute('insert into snake (name, species, length) values (?, ?, ?)',
            ('Python', 'Python regius', 183))
        conn.execute('insert into snake (name, species, length) values (?, ?, ?)',
            ('Boa', 'Boa constrictor imperator', 7))
        conn.execute('insert into snake (name, species, length) values (?, ?, ?)',
            ('Reticulated python', 'Python reticulatus', 6))
        conn.execute('insert into snake (name, species, length) values (?, ?, ?)',
            ('Corn
