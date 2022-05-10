import signal
signal.signal(signal.SIGINT, signal_handler)


def main():
    """Main method"""
    import argparse
    parser = argparse.ArgumentParser(
        description="Collection of functions for finding features"
    )
    subparsers = parser.add_subparsers()

    parser_gff = subparsers.add_parser("gff", help="Find features in GFF")
    parser_gff.add_argument('gff', type=str, help="GFF file")
    parser_gff.add_argument('-x', "--exact", type=str, default="",
                            help="Exact match. For example, 'gene' or 'mRNA'")
    parser_gff.add_argument('-r', "--regex", type=str, default="",
                            help="Regex matching. For example, 'gene.*' or "
                                 "'mRNA.*'")
    parser_gff.add_argument('-p', "--parent", type=str, default="",
                            help="Parent name
