import ctypes
ctypes.windll.kernel32.SetConsoleMode(ctypes.windll.kernel32.GetStdHandle(-11), 7)

def color_text(text, color, bold=False):
    """Returns the text with the given color"""
    # These are the ANSI escape codes used
    reset = "\033[0m"
    colors = {
        "red": "31",
        "green": "32",
        "yellow": "33",
        "blue": "34",
        "magenta": "35",
        "cyan": "36",
        "white": "37",
    }
    if color not in colors:
        return text

    return f'\033[{colors[color]}{";1" if bold else ""}m{text}{reset}'

def color_text_red(text, bold=False):
    """Shorthand for returning the text with the given color"""
    return color_text(text, "red", bold)

def color_text_green(text, bold=False):
    """Shorthand for returning the text with the given
