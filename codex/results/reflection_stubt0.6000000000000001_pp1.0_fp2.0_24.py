fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()
 
# Segmentation fault
"""

import sys

def main():
    sys.exit(1)

# __________  Entry point  __________

if __name__ == "__main__":
    main()
