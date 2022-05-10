import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)


def main():
    """Main entry point for the client."""
    # Create the top-level parser.
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(title='Commands',
                                       description='Valid commands',
                                       help='Additional help')

    # Create the parser for the "a" command.
    parser_a = subparsers.add_parser('a', help=do_a.__doc__)
    parser_a.set_defaults(func=do_a)

    # Create the parser for the "b" command.
    parser_b = subparsers.add_parser('b', help=do_b.__doc__)
    parser_b.set_defaults(func=do_b)

    # Parse the arguments.
    args = parser.parse_args()

    # Call the appropriate function.
    args.func(args)


