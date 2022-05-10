import mmap
+
+
+def generate_key_pair():
+    """Generates a new key pair"""
+    private_key = rsa.generate_private_key(
+        public_exponent=65537,
+        key_size=2048,
+        backend=default_backend()
+    )
+    public_key = private_key.public_key()
+    return private_key, public_key
+
+
+def encrypt_message(a_message, public_key):
+    """Encrypts a message with RSA-OAEP"""
+    return public_key.encrypt(
+        a_message,
+        padding.OAEP(
+            mgf=padding.MGF1(
+                algorithm=hashes.SHA256()
+            ),
+            algorithm=hashes.SHA256(),
+            label=None
+        )
+    )
+
+
+def decrypt_message(encrypted_message, private_key):
+    """Decrypts a message encrypted with RSA-OAEP"""
+    return private_
