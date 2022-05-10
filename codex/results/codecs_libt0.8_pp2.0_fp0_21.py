import codecs
codecs.register(lambda name: name == 'cp65001' and codecs.lookup('utf-8') or None)

from PyPDF2 import PdfFileWriter, PdfFileReader

files = [x for x in os.listdir('.') if x.endswith(".pdf")]

print(files)

output = PdfFileWriter()

for f in files:
    print("merging ", f)
    output.addPage(PdfFileReader(open(f, "rb")).getPage(0))

output_stream = open("merged.pdf", "wb")
output.write(output_stream)
output_stream.close()
