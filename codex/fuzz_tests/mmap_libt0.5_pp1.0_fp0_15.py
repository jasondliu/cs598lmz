import mmap
+from hashlib import md5
+from pathlib import Path
+from datetime import datetime
+from typing import Iterable
+from itertools import chain
+from collections import defaultdict
+from concurrent.futures import ProcessPoolExecutor
+
+
+def hash_file(filename: Path) -> str:
+    with filename.open('rb') as f:
+        return md5(mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)).hexdigest()
+
+
+def hash_files(files: Iterable[Path]) -> dict:
+    with ProcessPoolExecutor() as executor:
+        return {file: hash for file, hash in zip(files, executor.map(hash_file, files))}
+
+
+def find_duplicates(files: Iterable[Path]) -> dict:
+    hashes = hash_files(files)
+    duplicates = defaultdict(list)
+    for file, hash in hashes.items():
+        duplicates[hash].append(file)
