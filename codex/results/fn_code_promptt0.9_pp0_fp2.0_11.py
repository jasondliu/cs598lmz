fn = lambda: None
# Test fn.__code__

# Get current working directory.
# Path = os.getcwd()
# Change the working directory to specified path.
# os.chdir(Path)
# print("Current Working Directory " , Path)
 
# # Open a file
# fo = open(input('specify file name or type import/export/build: '), "r+")
# # fo.write('usjhbdsk' )
# str = fo.read()
# print ("Read String is : ", str)
# str = input()
# fo.write(str)

# Close opend file
# fo.close()
fn.__code__ = (lambda: None).__code__.replace(
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00",
    b"\x72\x34
