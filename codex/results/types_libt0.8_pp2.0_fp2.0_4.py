import types
types.ModuleType.check_module_usage = check_module_usage

##############################################################################

def main(namespace):
    """
    Run a main function obtained from a given namespace.
    """
    mainfunc = namespace.get('__main__')
    if mainfunc is None:
        # no main function found
        print("[Error] No '__main__' function found in namespace")
        return
    if not callable(mainfunc):
        # main function is not a function
        print("[Error] '__main__' is not callable")
        return

    # Call main function
    return mainfunc()

##############################################################################

def parse_args(namespace, argv=sys.argv[1:]):
    """
    Parse arguments in argv using an ArgumentParser obtained from the
    namespace.
    """
    argparser = namespace.get('__argparser__')
    if argparser is None:
        # default behaviour: no arguments
        return {}

    # Call parse_args method
    return argparser().parse_args(argv)
