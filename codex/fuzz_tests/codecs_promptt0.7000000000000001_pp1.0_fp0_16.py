import codecs
# Test codecs.register_error() before importing unicodedata
if sys.platform == "win32":
    import msvcrt
    msvcrt.setmode(sys.stdout.fileno(), os.O_BINARY)

try:
    unicodedata.lookup("TEST")
except KeyError:
    # this is the first time this is run
    try:
        unicodedata.lookup("TEST")
    except KeyError:
        # this is the second time this is run
        try:
            unicodedata.lookup("TEST")
        except KeyError:
            # this is the third time this is run
            try:
                unicodedata.lookup("TEST")
            except KeyError:
                # this is the fourth time this is run
                try:
                    unicodedata.lookup("TEST")
                except KeyError:
                    # this is the fifth time this is run
                    try:
                        unicodedata.lookup("TEST")
                    except KeyError:
                        # this is the sixth time this is run
                        try:
                            unicoded
