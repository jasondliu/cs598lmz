import codecs
codecs.register_error('strict', codecs.ignore_errors)

def main(argv):
  parser = argparse.ArgumentParser(description='Extracts the text from a PDF file.')
  parser.add_argument('pdf_path', help='Path to the PDF file.')
  parser.add_argument('output_path', help='Path to the output file.')
  args = parser.parse_args()

  pdf_path = args.pdf_path
  output_path = args.output_path

  if not os.path.exists(pdf_path):
    print 'The PDF path %s does not exist.' % pdf_path
    return 1

  # Load the PDF file.
  print 'Loading %s...' % pdf_path
  pdf_file = open(pdf_path, 'rb')
  pdf = PyPDF2.PdfFileReader(pdf_file)
  num_pages = pdf.getNumPages()
  print 'Loaded %s with %d page(s).' % (pdf_path, num_pages)

  # Extract the text from each page.
 
