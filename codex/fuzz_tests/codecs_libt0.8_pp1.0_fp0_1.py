import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'utf8mb4' else None)


class db_manager():
    """
    数据库管理器类
    """
    def __init__(self, db_name, db_username, db_password, db_address, db_port):
        """
        :param db_name: 数据库名称
        :param db_username: 数据库用户名
        :param db_password: 数据库密码
        :param db_address: 数据库地址
        :param db_port: 数据库端口
        """
        self.conn = pymysql.connect(host=db_address, port=db_port,
                                    user=db_username, password=db_password,
                                    db=db_name, charset='utf
