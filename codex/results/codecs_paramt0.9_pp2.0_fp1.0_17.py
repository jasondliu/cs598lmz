import codecs
codecs.register_error("strict", codecs.ignore_errors)
codecs.register_error("replace", codecs.replace_errors)

# set up the logging module
logging.basicConfig(level = 0, format = '%(asctime)s %(levelname)s: %(message)s')
module_logger = logging.getLogger('tm_client.common')
