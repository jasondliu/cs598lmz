import mmap
+
+def MigrateChunks(srcDump, dstDump, srcChunks, dstChunks, lenChunk, offset, limit):
+	with open(srcDump, 'rb') as srcFile:
+		with open(dstDump, 'rb+') as dstFile:
+			for i in range(0, limit): # offset ~ offset+limit-1
+				srcFile.seek(srcChunks[i+offset]*lenChunk)
+				dstData = srcFile.read(lenChunk)
+				dstFile.seek(dstChunks[i+offset]*lenChunk)
+				dstFile.write(dstData)
+
+def main():
+	args_parser = argparse.ArgumentParser(description='Data migration tool')
+	args_parser.add_argument('-s', dest='srcDump', nargs=1, help='Source dump path', required=True)
+	args_parser.add_argument('-d', dest
