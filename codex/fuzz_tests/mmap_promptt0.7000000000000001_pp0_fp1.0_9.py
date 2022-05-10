import mmap
# Test mmap.mmap(0, os.stat('/tmp/maptest').st_size, prot=mmap.PROT_READ)

def main():
    # Print a welcome message.
    print("Welcome to the Python Map Editor!")
    print()
    print("Type 'help' to get a list of commands.")
    print()

    # Create a new Map.
    map = Map()

    # Initialize the command loop.
    cmd = None
    while cmd != 'exit':
        # Print the prompt.
        sys.stdout.write('> ')

        # Read the command.
        cmd = sys.stdin.readline().strip().lower()

        # Handle the command.
        if cmd == 'help':
            print("The following commands are available:")
            print("   exit, quit, help, load, save, import, export, resize, addsquare, addsquareat, addsquareatworld, addroom, addroomat, addroomatworld, addopenrectangle, addopenrectangleat, addopenrectangleatworld, addportal, addportalat,
