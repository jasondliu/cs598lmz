import mmap
+
+def vec_to_file(vec, filename):
+    fvec = file(filename, "wb")
+    cPickle.dump(vec, fvec)
+    fvec.close()
+
+def file_to_vec(filename):
+    fvec = file(filename, "rb")
+    vec = cPickle.load(fvec)
+    fvec.close()
+    return vec
+
+def vec_to_mmap(vec, filename):
+    fvec = file(filename, "wb")
+    cPickle.dump(vec, fvec)
+    fvec.close()
+    mm = mmap.mmap(fvec.fileno(), 0)
+    fvec.close()
+    return mm
+
+if __name__=="__main__":
+    print "_________________________"
+    print "       Pickle Test"
+    print "_________________________"
+    print
+
+    import random
+    v = [random.randint(0,9999) for n in
