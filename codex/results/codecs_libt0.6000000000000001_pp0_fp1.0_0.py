import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# The directory containing the PDFs
pdf_folder = "C:/Users/cds/Dropbox/work/code/reports/"

# The directory to write the CSV files to
csv_folder = "C:/Users/cds/Dropbox/work/code/reports/csv/"

# The directory containing the tabula-java jar file
tabula_path = "C:/Users/cds/Dropbox/work/code/reports/tabula-0.9.2-jar-with-dependencies.jar"

# Loop through all of the files in the pdf_folder
for filename in os.listdir(pdf_folder):
    
    # Get just the file name without the extension
    file_name_no_extension = filename.rsplit('.', 1)[0]
    
    # Get the full path of the file
    file_path = pdf_folder + filename
    
    # Get the full path of the new CSV file
    csv_path = c
