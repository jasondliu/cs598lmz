import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 定义一个类，用于保存用户的基本信息
class User:
    def __init__(self, user_id, user_name, user_pwd, user_email, user_phone, user_type, user_status, user_create_time, user_update_time):
        self.user_id = user_id
        self.user_name = user_name
        self.user_pwd = user_pwd
        self.user_email = user_email
        self.user_phone = user_phone
        self.user_type = user_type
        self.user_status = user_status
        self.user_create_time = user_create_time
        self.user_update_time = user_update_time

# 定义一个类，用于保存
