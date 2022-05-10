from lzma import LZMADecompressor
LZMADecompressor.__bases__ = (pyfzf.Decompressor, )


def main():
    parser = argparse.ArgumentParser(
        usage="%(prog)s [options] <query>",
        description="A command-line fuzzy finder.",
        epilog="""
            Key bindings:
                <Ctrl-A>         Beginning of line
                <Ctrl-E>         End of line
                <Ctrl-H> <BS>    Delete left character
                <Ctrl-J> <C-J> <Enter> <Return>
                <Ctrl-K>         Delete to end of line
                <Ctrl-N> <Down>  Select next item
                <Ctrl-P> <Up>    Select previous item
                <Ctrl-U>         Delete to beginning of line
                <Ctrl-V>         Paste from clipboard
                <Ctrl-Y>         Paste from clipboard and select
                <Ctrl-X>         Toggle selection of current item
                <Ctrl-Z>         Unselect all items
                <Ctrl-Shift-A>   Select all items
                <Ctrl-Shift-N>   Select next
