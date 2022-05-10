import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# ======================================================================

class util_config:
    def __init__(self):
        self.cfg_file = "config.ini"
        self.cfg = configparser.ConfigParser()
        self.cfg.read(self.cfg_file, encoding="utf-8-sig")

    def add_section(self, section):
        if not self.cfg.has_section(section):
            self.cfg.add_section(section)

    def set_value(self, section, key, value):
        self.add_section(section)
        self.cfg.set(section, key, value)

    def get_value(self, section, key):
        self.add_section(section)
        if self.cfg.has_option(section, key):
            return self.cfg.get(section, key)
        return ""

    def save(self):
        with open(self.cfg_file, "w") as f:
            self
