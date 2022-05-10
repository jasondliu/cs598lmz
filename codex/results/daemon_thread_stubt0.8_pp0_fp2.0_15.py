import sys, threading

def run():
    user = sys.argv[1]
    password = sys.argv[2]

    # Create the connection to the database
    connection = pymysql.connect(host='localhost',
                                user=user,
                                password=password,
                                db='HW3',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
    # Read the query file
    q = open('queries.txt', 'r').read()
    queries = q.split(';')
    # Create the database
    with connection.cursor() as cursor:
        cursor.execute(queries[0])
    # Create the database
    with connection.cursor() as cursor:
        cursor.execute(queries[3])
    # Create the database
    with connection.cursor() as cursor:
        cursor.execute(queries[1])
    # Create the database
    with connection.cursor() as cursor:
        cursor.execute(queries[2])
    connection.commit()

run()
