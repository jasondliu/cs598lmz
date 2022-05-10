import select
# Test select.select()

def main():
    infile = open('/tmp/foo', 'r')
    infd = infile.fileno()
