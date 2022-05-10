import codecs
codecs.getwriter('utf-8')(sys.stdout)


def main():
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(process_data())


def process_data():
    global_data = {}
    global_data['migration'] = []

    # Get data from database
    database = MySQLdb.connect(host=config.host, user=config.user, passwd=config.passwd, db=config.db)
    cursor = database.cursor()
    cursor.execute('SELECT * FROM migrations WHERE migration_group = "add_user_required_groups";')
    results = cursor.fetchall()

    for row in results:
        migration = {}
        migration['id'] = row[0]
        migration['migration'] = row[1]
        migration['migration_group'] = row[2]
        global_data['migration'].append(migration)

    return global_data

if __name__ == '__main__':
    main()
