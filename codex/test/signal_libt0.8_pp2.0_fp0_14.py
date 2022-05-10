import signal
signal.signal(signal.SIGPIPE, signal.SIG_DFL)

# Verify command line arguments.
if (len(sys.argv) <= 1):
    print("Usage: %s <pdf-file> <output-file>" % sys.argv[0])
    sys.exit(1)

pdf_file = sys.argv[1]

# Create an output device that stores the resulting text.
device = textout.TextConverter(sys.stdout, codec='utf-8')
# Create a PDF interpreter object.
interpreter = PDFInterpreter(rsrcmgr, device)

pdf_file_handle = file(pdf_file, 'rb')

# Process each page contained in the document.
for page in PDFPage.get_pages(pdf_file_handle):
    interpreter.process_page(page)
