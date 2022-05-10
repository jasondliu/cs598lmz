fn = lambda: None
# Test fn.__code__.co_argcount
fn.__code__ = Mock()
fn.__code__.co_argcount = 3
fn(1, 2)


class MockParseArgs:
    def __init__(self):
        self.host = 'host'
        self.port = 'port'


class MockConfigParser:
    def __init__(self):
        self.config_file = 'config_file'
        self.config = Mock()
        self.config.parse_args = MockParseArgs()


def mock_config_parser():
    return MockConfigParser()


def mock_config_parser_key_error():
    parser = MockConfigParser()
    parser.config.parse_args = MockParseArgs()
    parser.config.parse_args.host = 'host'
    parser.config.parse_args.port = 'port'
    return parser


def mock_backup_config():
    return {'host': 'host', 'port': 'port'}


def mock_backup_config_key_error():
    return {'host':
