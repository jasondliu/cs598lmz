import mmap
+
+import pandas as pd
+
+from cliwh import cliwh as cli
+
+from ooi_data.postgres.model import Stream, StreamParameter
+
+
+# Parse command line arguments
+parser = cli(description="Convert stream metadata to 'json' format.")
+
+parser.add_argument(
+    '-i', '--input',
+    help="Input 'json' file with stream metadata.",
+    type=str,
+    required=True
+)
+
+parser.add_argument(
+    '-o', '--output',
+    help="Output directory for streams.",
+    type=str,
+    required=False,
+    default=os.getcwd()
+)
+
+parser.add_argument(
+    '-m', '--mmap',
+    help="Memory map output files.",
+    action='store_true'
+)
+
+args = parser.parse_args()
+
+
+args.output = os.path.abspath
