import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)


def get_con_all_words(cursor, table_name, id_col='id'):
    """
    所有评论的文本, 用来训练词向量
    :param cursor:
    :param table_name:
    :param id_col:
    :return:
    """
    # 所有评论的文本, 用来训练词向量
    cursor.execute(
        'SELECT {id_col}, content FROM {table_name}'.format(table_name=table_name, id_col=id_col)
    )
    words_list = [i[1] for i in cursor.fetchall()]
    words = "".join(words_list)
    return words


def get_con_all_words_for_one(cursor,
