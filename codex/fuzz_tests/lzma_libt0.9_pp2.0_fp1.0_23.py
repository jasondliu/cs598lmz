import lzma
lzmaModule = True
except ImportError:
lzmaModule = False
def main(argv = None):
    import sys
    if argv is None:
        argv = sys.argv
    if len(argv) != 3:
        print("Usage: %s %s %s" % (
            sys.executable, os.path.basename(argv[0]),
            "<compressed file> <uncompressed output>"),
              file=sys.stderr)
        print("""Let <compressed file> be the name of a file containing
binary data that was compressed using xz. <uncompressed output>
is the name of the file the content of <compressed file>
is written to after decompression.""",
              file=sys.stderr)
        return 1
    if lzmaModule:
        with lzma.open(argv[1], "rb") as c:
            with open(argv[2], "wb") as u:
                shutil.copyfileobj(c, u)
    else:
        with open(argv
