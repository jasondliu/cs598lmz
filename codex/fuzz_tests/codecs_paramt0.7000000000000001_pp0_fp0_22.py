import codecs
codecs.register_error('replace_spaces', lambda e: (unicode(' '), e.start + 1))

# TODO - add "crawl_all" option to crawl all pages
# TODO - add "debug" option to output debugging messages
# TODO - add "logging" option to log the output
# TODO - add "log_level" option to set the logging level
# TODO - add "log_max_size" option
# TODO - add "log_max_files" option


# Configuration
# -------------
class Config(object):
    def __init__(self):
        self.output_dir = '.'
        self.output_format = 'text'
        self.output_file_prefix = 'crawl'
        self.output_file_suffix = ''
        self.output_file_extension = '.txt'
        self.output_file_name = '{0}{1}{2}'.format(self.output_file_prefix, self.output_file_suffix, self.output_file_extension)
        self.output_file_path = os.
