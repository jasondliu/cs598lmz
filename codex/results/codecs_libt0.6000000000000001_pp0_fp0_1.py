import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)


def get_connection():
    """
    Get database connection
    :return: database connection
    """
    try:
        conn = mysql.connector.connect(user=settings.DB_USER, password=settings.DB_PASS, database=settings.DB_NAME,
                                       host=settings.DB_HOST, port=settings.DB_PORT)
        return conn
    except:
        return None


def get_query_results(query, values=None):
    """
    Run a query on database
    :param query: query to be run
    :param values: values to be binded with query
    :return: result set
    """
    try:
        conn = get_connection()
        if conn is None:
            return None
        cursor = conn.cursor()
        if values:
            cursor.execute(query, values)
        else:
            cursor.execute(query)
        result = cursor.fetchall()
        conn.close
