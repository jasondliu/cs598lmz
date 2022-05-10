import mmap
+import re
+import os
+import random
+import sqlite3
+import argparse
+from multiprocessing import Pool
+
+def is_valid_file(parser, arg):
+    if not os.path.exists(arg):
+        parser.error("The file %s does not exist!" % arg)
+    else:
+        return arg
+
+def parse_args():
+    """parse arguments"""
+    parser = argparse.ArgumentParser(description=__doc__,
+        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
+    parser.add_argument('-f', '--fasta', type=lambda x: is_valid_file(parser, x),
+        help="read FASTA file [%(default)s]", default="test.fa")
+    parser.add_argument('-o', '--output_dir', type=str,
+        help="output directory [%(default)s]", default=".")
+    parser.add_argument('-r', '--random_seq
