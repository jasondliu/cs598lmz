import threading
threading.stack_size(67108864)

try:
    from . import parsing, utils, report
    from .utils import PARSER_HELP
    from .parsing import parse_args, parse_config
    from .report import smtp_notify
except SystemError:
    import parsing
    import utils
    import report
    from utils import PARSER_HELP
    from parsing import parse_args, parse_config
    from report import smtp_notify


def main():
    """
    Entry point for the script
    """
    args = parse_args()
    utils.logger.info('Script has started running')
    config = parse_config(args.config)

    if config['report']:
        thread = threading.Thread(target=smtp_notify, args=(config,), kwargs={'message_error': PARSER_HELP})
        thread.start()

    utils.logger.info('Running parsing of sites')
    are_parsers_run = parsing.core.run_p
