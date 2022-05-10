import codecs
codecs.register(Codec.search_function)

import imp
import sys

# Get TextMate-specific modules
bundle = Bundle.bundle()
sys.path.append(os.path.expanduser('~/Library/Application Support/TextMate/Pristine Copy/Bundles/CoffeeScript.tmbundle/Support'))
tm_support = imp.load_source('tm_support', 'tm_support.py')

def run_command(fun, file_=None):
    try:
        # First test for exception info, since it can contain newlines
        m = re.match(r'^(?P<exception>Traceback \(most recent call last\):)(?P<message>.*?)(?P<error_line>File "[^ ]+", line (?P<line_no>[0-9]+))?\n', tm_support.html_error(''))
        if m:
            error_format = '%s<br/><span class="line"><code><span class="syntaxerror">%s</span></code
