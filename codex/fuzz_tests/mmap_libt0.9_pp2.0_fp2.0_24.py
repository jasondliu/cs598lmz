import mmap
+
+def _control_parser(args):
+    parser = argparse.ArgumentParser(prog=sys.argv[0],
+                                     description='Analyze a pyc file.',
+                                     usage='`%(prog)s COMMAND --help` for help on a command.',
+                                     epilog='You can also start %(prog)s in interactive mode without any argument.',
+                                     add_help=True,
+                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
+    parser.add_argument('--version', action='version', version='1.0.0')
+    subparsers = parser.add_subparsers(title='Available commands', dest='command')
+    subparsers.required = True
+    for command in _commands:
+        command(subparsers)
+    args = parser.parse_args()
+    return args
+
+
+class InteractiveArgumentParser(argparse.ArgumentParser):
+    """ArgumentParser that prints help message in
