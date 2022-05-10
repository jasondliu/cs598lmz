import _struct
+from collections import defaultdict
+from io import BytesIO
+from pathlib import Path
+from itertools import chain
+from functools import reduce
+from operator import or_
+from typing import Union, List, Dict, Tuple, Any
+
+
+def get_solids(file_path: Union[Path, str],
+               block_palette: Dict[str, int]) -> List[Dict[str, Union[int, List[int]]]]:
+    """Given a file path and a block palette, returns a list of all solid blocks in the given world."""
+    # Read in the world file as a byte stream
+    world_file = BytesIO(open(file_path, "rb").read())
+
+    def read_chunk_section_block_array(block_array: bytes,
+                                       palette: List[Dict[str, int]]) -> List[Dict[str, Union[int, List[int]]]]:
+        """Reads a block array and returns the blocks in a format that's easier to work
