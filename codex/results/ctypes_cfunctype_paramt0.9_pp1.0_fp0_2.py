import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

builtin_dict = globals().copy()
builtin_dict.update(locals())
builtin_dict["__name__"] = "__main__"
builtin_dict["__file__"] = os.path.abspath(sys.argv[0])
builtin_dict["__builtins__"] = __builtins__
builtin_dict["logger"] = logger
builtin_dict["settings"] = settings
builtin_dict["FUNTYPE"] = FUNTYPE
builtin_dict["ConfigParser"] = ConfigParser.ConfigParser
builtin_dict["event_callback"] = event_callback

# read initial projecs
projects = None
projects = ConfigParser.ConfigParser()
projects.read(".mymonkey")


# read commandline options
parser = OptionParser()

default_mode = "cli" if sys.argv[1:] and sys.argv[1] != "gui" else "gui"

parser.add_option("--mode", default=default_mode, action="store")
