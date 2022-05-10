import lzma
lzma.LZMAError:
    print("LZMA compression is not available")
    sys.exit(1)

from . import __version__

def main():
    parser = argparse.ArgumentParser(
        description="A tool to create and extract archives in the LZMA format",
        epilog="""
        Examples:
        lzma e archive.lzma       Extract archive.lzma
        lzma d archive.lzma       Decompress archive.lzma
        lzma a archive.lzma file  Add file to archive.lzma
        lzma a archive.lzma dir/* Add all files from directory to archive.lzma
        lzma l archive.lzma       List contents of archive.lzma
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        )
    parser.add_argument("-V", "--version", action="version",
                        version="%(prog)s " + __version__)
    parser.add_argument("-v", "--verb
