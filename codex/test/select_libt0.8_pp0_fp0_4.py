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
        
