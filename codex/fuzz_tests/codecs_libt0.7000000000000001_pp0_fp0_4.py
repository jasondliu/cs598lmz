import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

#
#
#
def main():
    #
    #
    #
    print("Welcome to the dumb file renamer.")

    #
    #
    #
    print("\n")
    file_directory = input("Enter a valid file directory.\n")
    
    #
    #
    #
    print("\n")
    file_extension = input("Enter the file extension you wish to rename.\n")
    
    #
    #
    #
    print("\n")
    rename_to = input("Enter the file extension you wish to rename to.\n")

    #
    #
    #
    print("\n")
    confirm = input("Confirm you wish to rename all " + file_extension + " files to " + rename_to + " in this directory.\n")
    if confirm == "yes":
        #
        #
        #
        files = glob.glob(file_directory + "*
