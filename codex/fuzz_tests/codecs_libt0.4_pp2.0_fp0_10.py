import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

#-------------------------------------------------------------------------------
# Global variables
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# Classes
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# Functions
#-------------------------------------------------------------------------------

def main():
    """
    Main function
    """
    # Parse command line arguments
    args = parse_arguments()

    # Read the file
    with open(args.input_file) as f:
        content = f.readlines()

    # Remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]

    # Write the file
    with open(args.output_file, 'w') as f:
        for line in content:
            f.write(line)
            f.write('\n')

#-------------------------------------------------------------------------------

def parse_arguments():
    """
    Parse command line arguments
    """
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Convert a file
