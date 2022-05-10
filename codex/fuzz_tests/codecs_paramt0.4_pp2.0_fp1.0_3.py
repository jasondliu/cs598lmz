import codecs
codecs.register_error('surrogate_escape', codecs.backslashreplace)

# The regexes used to parse the log file
re_log_line = re.compile(r'^\[(?P<timestamp>.*)\] (?P<message>.*)')
re_log_line_with_context = re.compile(r'^\[(?P<timestamp>.*)\] (?P<context>.*): (?P<message>.*)')
re_log_line_with_context_and_level = re.compile(r'^\[(?P<timestamp>.*)\] (?P<level>\w+): (?P<context>.*): (?P<message>.*)')
re_log_line_with_level = re.compile(r'^\[(?P<timestamp>.*)\] (?P<level>\w+): (?P<message>.*)')

# The regexes used to parse the log message
re_log_message = re.compile(r'^(?P<message>
