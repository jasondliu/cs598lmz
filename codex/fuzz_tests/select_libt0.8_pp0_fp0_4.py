import select

def loop(socket, db, user, password, *args, **kwargs):
    connection = db.connect(user=user, password=password)
    cursor = connection.cursor()
    cursor.execute('use %s' % settings.DATABASE_NAME)

    while True:
        inputs, outputs, errors = select.select([socket], [], [socket])

        for input in inputs:
            user_id, data = input.recvfrom(1024)
            handle_data(user_id, data, cursor)
        
        for error in errors:
            print 'Error: %s' % error


def handle_data(user_id, data, cursor):
    print 'Processing data'
    #TODO check if user is registered
    #TODO count total KG (PARSE)
    #TODO calculate footprint of each KG
    #TODO update user's footprint


if __name__ == '__main__':
    loop(*args, **kwargs)
