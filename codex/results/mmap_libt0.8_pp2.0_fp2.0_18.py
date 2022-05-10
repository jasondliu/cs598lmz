import mmap
+
+parser = argparse.ArgumentParser(prog='count_fasta_recs.py',
+																 description='''Count the number of fasta records in a fasta file,
+																 by looking for record headers.''')
+parser.add_argument('fasta_file', help='fasta file to search')
+args = parser.parse_args()
+
+# to search binary file (doesn't load in memory)
+with open(args.fasta_file, 'rb', 0) as file, \
+		mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as s:
+	rec_count = 0
+	pos = s.find(b'>')
+	while pos != -1:
+		rec_count += 1
+		pos = s.find(b'>', pos+1)
+	print(rec_count)
+
+
+
