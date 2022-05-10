import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)


def query2update(sql, table_name, connection=None, cursor=None):
    """
    query-like sql to update-like sql
    :param sql:
    :param table_name:
    :param cursor:
    :return:
    """
    if cursor is None:
        connection = get_connection()
        cursor = connection.cursor()

    update_sql = "UPDATE " + table_name + " SET "
    select_sql = "SELECT "
    where_sql = ""

    where_pos = sql.rfind("WHERE")
    if where_pos != -1:
        where_sql = sql[where_pos:]
        sql = sql[:where_pos]

    sql_words = sql.split()
    pk = table_pk(table_name, connection=connection, cursor=cursor)
    update_fields = []
    for word in sql_words:
        if word == "*" or word == "SELECT
