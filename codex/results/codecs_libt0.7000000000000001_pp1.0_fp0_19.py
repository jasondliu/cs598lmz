import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

class BotConfig:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        self.token = self.config['BOT']['Token']
        self.prefix = self.config['BOT']['Prefix']
        self.roleCount = int(self.config['BOT']['RoleCount'])
        self.roleName = self.config['BOT']['RoleName']
        self.rolePrefix = self.config['BOT']['RolePrefix']
        self.roleSuffix = self.config['BOT']['RoleSuffix']
        self.roleHex = self.config['BOT']['RoleHex']

    def get_token(self):
        return self.token

    def get_prefix(self):
        return self.prefix
    
    def get_role_count(self):
        return self.
