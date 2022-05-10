import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_term_colors():
    if not sys.stdout.isatty():
        return False
    try:
        import curses
        curses.setupterm()
        return curses.tigetnum('colors') >= 8
    except Exception:
        return False

term_colors = get_term_colors()

def colored(text, color=None, on_color=None, attrs=None):
    if term_colors:
        if color:
            text = '\x1b[%dm%s' % (color, text)

        if on_color:
            text = '\x1b[%dm%s' % (on_color, text)

        if attrs:
            text = '\x1b[%dm%s' % (attrs, text)

        text += '\x1b[0m'

    return text

class Color(object):
    BLACK = 30
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE =
