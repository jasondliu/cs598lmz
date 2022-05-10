import codecs
codecs.set_encoding("utf-8")

class Config(object):
    def __init__(self, config_name, config_path):
        _config_path = config_path
        with codecs.open(_config_path, "r", encoding="utf-8") as f:
            raw_data = f.read()
        try:
            configs = json.loads(raw_data)
            assert isinstance(configs, dict)
        except:
            raise Exception("Wrong in json file %s" % _config_path)
        for k, v in configs.items():
            assert isinstance(k, str) and isinstance(v, dict)
            assert set(v.keys()) == {"url_prefix", "host", "port",
                                     "database", "attrs"}
        self.configs = _ConfigMap(configs)
        self.config_name = config_name
        config = configs[config_name]
        self.config = _ConfigWrapper(config)
        self._attrs = set(self.config.attrs.
