import _struct
+
+
+
+def main():
+
+    inFile = 'sigmod_srds.pdf'
+    outFile = 'sigmod_srds.txt'
+
+    fp = open(inFile, 'rb')
+    pdf = PyPDF2.PdfFileReader(fp)
+    numPage = pdf.numPages
+    print(numPage)
+
+    fpOut = open(outFile, 'wt')
+
+    for p in range(numPage):
+        page = pdf.getPage(p)
+        content = page['/Contents'].getObject()
+        if not isinstance(content, PyPDF2.generic.IndirectObject):
+            raise TypeError(
+            'Unexpected object type: %s' % type(content))
+
+        content = PyPDF2.PDFStream(content)
+        decoded = content.getData()
+        stream = PyPDF2._py3k.StringIO(decoded)
+        h = _struct.Struct('!I
