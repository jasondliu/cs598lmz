import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 数据库配置
configs = config_default.configs

try:
    import config_override
    configs = merge(configs, config_override.configs)
except ImportError:
    pass

# 初始化数据库连接
# __all__ = ['create_engine']

def create_engine(user, password, database, host='127.0.0.1', port=3306, **kw):
    """
    db模块核心函数，用于连接MySQL数据库并生成操作游标
    :param user: 连接数据库用户名
    :param password: 连接数据库
