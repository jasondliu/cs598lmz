import codecs
codecs.register_error('ignore', codecs.ignore_errors) # http://stackoverflow.com/a/18561496

# Suppress tkinter window
root = tkinter.Tk()
root.withdraw()

def main():
    book_title = askopenfilename(defaultextension=".epub", filetypes=[("EPUB", "*.epub"), ("all files", "*.*")], title="Select file to convert")
    
    if book_title[-5:].lower() == ".epub" or book_title[-4:].lower() == ".kep":
        convert_to_anki(book_title)
        copyfile(book_title, book_title[:-4] + "_backup" + book_title[-4:])
        system("del " + book_title)
    else:
        print("Not an EPUB file.")
        input("Press enter to close.")

def convert_to_anki(book_title):
    print("Converting " + book_title + "...")
    temp_file = write_to_ank
