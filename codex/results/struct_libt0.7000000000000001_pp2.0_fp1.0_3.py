import _struct
+
+def get_info(id, info_type="fast", seq_type=None, get_seq=True):
+    """
+    Retrieves information about a UniProt entry.
+
+    Parameters
+    ----------
+    id : str
+        UniProt ID.
+    info_type : str
+        Type of information.
+        Either "fast" or "full".
+    seq_type : str
+        Type of sequence.
+        Either "canonical" or "all".
+    get_seq : bool
+        Whether to return the sequence of the protein.
+
+    Returns
+    -------
+    info : str
+        Information on the entry.
+    """
+    if info_type not in ("fast", "full"):
+        raise ValueError("Invalid value for 'info_type': %s" % info_type)
+    if info_type == "fast" and seq_type is not None:
+        raise ValueError("'seq_type' can only be set with 'info_type=\"full\"'")
